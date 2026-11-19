# Profile artwork

The DraveNIQ signature is the supplied **Inside the Coil** arrangement from
`DraveNIQ_Logo_Kit.zip` (`01_Logos/02_Inside_the_Coil.png`). The PNG is preserved
byte-for-byte; the profile banner embeds it without changing its proportions,
orientation, colours or lettering. Its background is opaque.

SHA-256: `4db41e57f2d752a92290aeb29687e0be196c1f591d447c7c151c734ffe2f9bf1`

The surrounding composition uses Deep Navy `#060A12`, Drave White `#EDF3F5`,
Electric Azure `#168BEE`, Ice Blue `#72D7FF`, Cobalt `#2052C8`, and Drave Coral
`#ED8179`. The personal name remains primary; DraveNIQ is the creative identity.

Project illustrations are original concepts for this profile. They are not
product screenshots, robot recordings or experiment results.

Run `python3 scripts/build_profile_covers.py` from the repository root to
regenerate the desktop, mobile and still headers and four project covers.
Use `--check` to verify that checked-in output matches the generator.
All SVGs are self-contained: no remote font, image service or script is needed.
All desktop, mobile and separately linked still headers are static. The shorter
role-led composition keeps the person and engineering focus primary, with the
original DraveNIQ signature as the supporting identity.

The mobile navy source comes before the desktop light/dark choice in the
README. GitHub rewrites colour-scheme source conditions to match its own theme;
combining a width query with that condition can lose the width constraint.
Keeping the width-only source first preserves mobile art direction in either
GitHub theme. The light mobile asset is retained as an alternative artwork.
