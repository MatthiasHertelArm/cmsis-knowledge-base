---
id: "ceed-test-suite-report-log-factory-creating-a-custom-report"
type: "concept"
domain: "test"
title: "Test Suite Report Log Factory: Creating a Custom Report"
summary: "Creating your own report requires three steps:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/report-tests-log-factory.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-log-factory/#creating-a-custom-report"
license: "MIT"
mode: "V"
---

Creating your own report requires three steps:

1. Choose a directory to hold your report Ruby code and add it to your `:plugins` ↳ `:load_paths` configuration.
1. Create a Ruby file in the directory from (1) per instructions that follow.
1. Enable your new report in your `:report_tests_log_factory` Ceedling configuration.

### Custom report configuration

Configuration steps, (1) and (3) above, are documented by example below. Conventions simplify the Ruby programming and require certain naming rules that extend into your project configuration.

```yaml
:plugins:
  :load_paths:              # Paths can be relative or absolute
    - scripts/              # Add <build root>/scripts to Ruby’s load paths
  :enabled:
    - report_tests_log_factory

:report_tests_log_factory:
  :reports:
    - fancy_shmancy         # Your custom report must follow naming rules (below)
```

### Custom `TestsReporter` code

To create a custom report, here’s what you gotta do:

1. Create a Ruby file in your configured additional load path named `<custom_report>_tests_reporter.rb`. `<custom_report>` should be in lower case and use underscores if you wish to separate words (i.e. snakecase).
1. The Ruby code itself must subclass an existing plugin class, `TestsReporter`.
1. Your new subclass must be named `<CustomReport>TestsReporter` where `<CustomReport>` is the camelcase version of your report name from (1).
1. Fill out up to four methods in your custom `TestsReporter` subclass:
    * `setup()`
    * `header()` (optional)
    * `body()`
    * `footer()` (optional)

    `header()`, `body()`, and `footer()` each receive the same four keyword
    arguments — `stream:`, `name:`, `results:`, and `duration_s:` — whether
    or not your own implementation needs all of them.

Overriding the default filename of your custom report happens just as it does for the built-in reports. In fact, apart from the custom load path, the built-in reports documented above use the same mechanisms as a custom report. These Ruby files can and should be used as references.

You may access `:report_tests_log_factory` configuration for your custom report using a handy utility method documented in a later section.

#### Sample `TestsReporter` custom subclass

The following code creates a simple, dummy report of the _FancyShmancy_ variety (note the name correspondence to the example configuration YAML above).

```ruby
# Must include this `require` statement
require 'tests_reporter'

# Your custom class must:
#  1. Follow the naming convention <CustomReport>TestsReporter where 
#     <CustomReport> corresponds to the <custom_report> entry in your 
#     `:report_tests_log_factory` configuration.
#  2. Subclass `TestsReporter`.
class FancyShmancyTestsReporter < TestsReporter

  # Must include a method `setup()` that:
  #  1. Calls `super()` with a default filename for the custom report.
  #     (No convention or limitations on filenames.)
  #  2. Includes any needed instance variables.
  #     (`setup()` is effectively your constructor.)
  def setup()
    super( default_filename: 'fancy_shmancy_tests_report.xml' )
  end
  
  # If your report includes a header section, fill out this method.
  # If no header in your report, this method is not needed in this file at all.
  def header(stream:, name:, results:, duration_s:)
    stream.puts( '<?xml version="1.0" encoding="utf-8" ?>' )
    stream.puts( "<FancyShmancy Name=\"#{xml_escape( name )}\" TestCount=\"#{results[:counts][:total]}\">" )
  end

  # Process test results into report records.
  # Each outcome category lists test files, each with a collection of test cases.
  def body(stream:, name:, results:, duration_s:)
    [:successes, :failures, :ignores].each do |category|
      results[category].each do |result|
        result[:collection].each do |item|
          write_test( item, stream )
        end
      end
    end
  end

  # If your report includes a footer section, fill out this method.
  # If you have no footer in your report, this method is not needed in this file at all.
  def footer(stream:, name:, results:, duration_s:)
    stream.puts( "</FancyShmancy>" )
  end

  # If you want to break up your custom reporting code, create all the private 
  # methods you wish and call them as needed from `setup()`, `header()`, 
  # `body()`, and `footer()`.

  private

  # A simple helper method for a simple test report entry.
  # This method is not required by a custom `TestsReporter` subclass.
  def write_test(item, stream)
    stream.puts( "  <Test><Name>#{xml_escape( item[:test] )}</Name></Test>" )
  end

end
```

#### Plugin hooks & test results data structure

See [_PluginDevelopmentGuide_][custom-plugins] for documentation of the test results data structure (i.e. the `results` method arguments in above sample code).

See this plugin’s built-in `TestsReporter` subclasses — `json_tests_reporter.rb`, `junit_tests_reporter.rb`, `cppunit_tests_reporter.rb`, and `html_tests_reporter.rb` — for examples of using test results.

[custom-plugins]: ../development/plugins/index.md

#### `TestsReporter` utility methods

##### Configuration access: `fetch_config_value(*keys)`

You may call the private method `fetch_config_value(*keys)` of the parent class `TestsReporter` from your custom subclass to retrieve configuration entries.

This method automatically indexes into `:report_tests_log_factory` configuration to extract any needed configuration values for your custom report. If the configuration keys do not exist, it simply returns `nil`. Otherwise, it returns the hash, list, string, boolean, or numeric value for the specified key walk into your report’s configuration.

`fetch_config_value(*keys)` expects a list of keys and only accesses configuration beneath `:report_tests_log_factory` ↳ `:<custom_report>`.

###### Example _FancyShmancy_ configuration + `TestsReporter.fetch_config_value()` calls

```yaml
report_tests_log_factory:
  :fancy_shmancy:
    # Hypothetical feature to standardize test names before writing to report
    :standardize:
      :names: TRUE
      :filters:
        - '/^Foo/'
        - '/Bar$/'
```

```ruby
# Calls from within FancyShmancyTestsReporter

fetch_config_value( :standardize, :names ) => true

fetch_config_value( :standardize, :filters ) => ['/^Foo/', '/Bar$/']

fetch_config_value( :does, :not, :exist ) => nil
```

##### Markup escaping: `xml_escape(str)` and `html_escape(str)`

Test names, messages, filepaths, and your project name can all contain characters that are significant in markup, such as `&`, `<`, and `"`. Pass each such value through the private method `xml_escape()` or `html_escape()` before writing it into an XML or HTML report. Without escaping, a single unusual test name produces a report that report processing tools reject.

Both methods return a new string. Never modify the `results` structure in place. Every configured report receives the very same `results`.
