---
id: "intr-the-android-developer-s-journey-in-evolution-of-observability"
type: "concept"
domain: "debug"
title: "The Android Developer's Journey into Hardware Observability: Evolution of observability"
summary: "If you're developing Android hardware, it's likely the core of your device is several standard Android mobile apps, and you can start by using the mature ecosystem of Android app observability tools like Crashlytics, Bugsnag, Instabug, or others, …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-28-aosp-observability.md"
doc_source: "https://interrupt.memfault.com/blog/aosp-observability#evolution-of-observability"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you're developing Android hardware, it's likely the core of your device is
several standard Android mobile apps, and you can start by using the mature
ecosystem of Android app observability tools like Crashlytics, Bugsnag,
Instabug, or others, to maintain the quality of those apps.

### User error reports

The first hiccup in development often arises when a user encounters a bug not
captured by existing app observability tools. User error reports can be quite
vague (e.g., "the screen just went black!"), making it essential to gather more
information from the affected device. Early in the process of Android
development, many developers come across
[Android bug reports](https://developer.android.com/studio/debug/bug-report),
which often leads to establishing a process for users to generate and share
these reports. In some cases, the app can guide users through creating a bug
report and then emailing it to the engineering team.


    
        
    
    Telescope GitHub library


There are many obvious problems with this approach: they might already be
unhappy with the experience and unwilling to cooperate; they might have returned
the product already; they might be busy and miss the message. But if there is a
low number of devices in the field, this can feel somewhat sustainable with only
minimal engineering effort.

### Automatic error reports

Of course, as there are more users, we can improve the process here by spending
more engineering time to reduce the time the customer spends. We can first focus
on automating the bug report collection to avoid having the customer do the work
— when they call in with an issue, we can remotely trigger a bugreport for
them and then write code to asynchronously upload the report in the background.
To trigger the upload, we can develop a new native service in our AOSP build to
listen for a push notification. This might be a big feature in itself if push
notifications are not supported.

Then, we'll have to find a sustainable, secure location to upload the bugreports
to. To start, we could compromise: the bugreports can be sent to a personal
email in the interim, the bugreports might never expire, or the bugreports might
be uploaded into an existing system that wasn't meant to handle that file size
or volume. But it should work, and once we can download the bugreport, it often
has enough information for us to find the bug.

### Capturing device logs

After automatic error upload, we likely encounter situations where the
bugreports might not be enough. So we get the idea to upload the device logs as
well. We'll quickly discover the different types of
[logcat buffers](https://developer.android.com/tools/logcat) on the device: like
`main`, `system`, or `crash`, and see that some kernel errors showed up in the
system buffer in the past. The size of the buffers are quite small, so you might
have to find ways to increase the size of the buffers to persist them for
longer. And it could make sense to append these device logs onto the same
bugreport system as before.

### Reactive improvements

Over time, this process could improve iteratively, as it's generally good
enough, and we end up being tasked to work on other projects until there's a
fire requiring us to capture more information we don't have. If there isn't
enough data in the bugreport, or in the device logs, there might be more areas
of AOSP to query and add to be uploaded, like tombstone files, dumpsys, or
recovery logs, or the many system services. We may eventually refine the backend
too, so there's a dedicated area for viewing all the uploaded data by a single
device or by user.
