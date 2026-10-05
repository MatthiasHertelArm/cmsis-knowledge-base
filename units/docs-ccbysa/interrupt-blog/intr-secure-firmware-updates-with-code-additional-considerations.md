---
id: "intr-secure-firmware-updates-with-code-additional-considerations"
type: "concept"
domain: "debug"
title: "Secure firmware updates with code signing: Additional Considerations"
summary: "Your firmware signing process is only as secure as your key storage mechanism. Since the private key can be used to create build that look like they are coming from you, it is important to keep it private."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-08-secure-firmware-updates-with-code-signing.md"
doc_source: "https://interrupt.memfault.com/blog/secure-firmware-updates-with-code-signing#additional-considerations"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Key Storage

Your firmware signing process is only as secure as your key storage mechanism.
Since the private key can be used to create build that look like they are coming
from you, it is important to keep it private.

Your key storage system needs to:
1. Put the key out of reach of most employees / partners
2. Make it easy to sign a release build you actually want signed
3. Be resilient. If you lose the key, you won't be able to distribute additional
   firmware updates.

Unfortunately, this is not easy to do. Many people simply store their private
key alongside their source code, in their git repoitory. Do not do this! It
fails to meet rule (1) and is considered poor practice (in fact, Github will
warn you if it detects something that looks like a private key in your
repository).

Instead, it is better to store your key alongside your [CI system](https://interrupt.memfault.com/blog/continuous-integration-for-firmware) and let it handle signing of
release builds. Make sure only select users have access to the private key, by
restricting permissions in your CI system. Most systems support this use case
one way or another. For example, CircleCI offers [Restricted
Contexts](https://circleci.com/docs/2.0/contexts/#restricting-a-context) which
can be set up such that only administrator level users can see a private key,
and their approval is needed to trigger a release build.

You may take key storage a step further and use a specialized Secrets Management
Systems such as Hashicorp Vault[^vault] or Amazon Key Management Service[^kms].
These are systems that offer secure secret storage with complex access control
lists and API integrations.

Last but not least, make sure to securely store a backup of your keys somewhere.
Whether on paper, on a smartcard, or on an airgapped system, your offline
backups should be inaccessible most of the time.

### Key Rotation

In the event a private key gets compromised, we need the ability to rotate it.
This involves generating a new public / private key pair, and updating the
public key hardcoded in the firmware.  Thankfully, this is a relatively simple
process with our current architecture. Since the public key is hardcoded in
updateable components, we simply update them!

Here are the step-by-step details:
1. Generate a new private/public key pair with `openssl`
2. Hardcode  the new public key in our Updater and Loader firmware
3. Build a new Updater, sign it with the *old* private key
4. Build a new Loader, sign it with the *new* private key
5. Build a new Application, sign it with the *new* private key
6. Load the new Updater on your devices. Because it is signed with the old key,
   the current Loader will accept it.
7. Load the new Loader on your devices via the new Updater
8. Load the new Application on your devices via the new Loader

As you see, this is the same process we'd use to update the Loader for any other
reason.

### Development Keys

Since we've taken great pains to make sure our engineers do *not* have direct
access to the key, how can we enable them to load custom firmware images on
their development devices?

We need a set of development keys which are used for that use case only. All
development systems have the development public key hardcoded in rather than the
production key. The development private key can only be used to sign firmware
for these development systems, so it isn't sensitive and can be stored in the
repository.

Production systems should continue to use the production key, and will not
accept firmware signed with the development key. In the event we want to load a
development build on a production system - say, for debugging - we load a
special Loader on it which is signed with the production key but contains the
development key. This special Loader must be safeguarded: it downgrades
verification on a production system to an insecure key.
