# TITAN PRO Android project

Python/Flask dashboard packaged via python-for-android WebView bootstrap.

Build on Linux/WSL2 (requires Android SDK/NDK downloads and internet):
```bash
pip install --upgrade buildozer
buildozer android debug
```
APK output: `bin/`.

The application data paths are locked to `/storage/emulated/0/LLL`. Modern Android scoped storage may block arbitrary shared-folder writes; the legacy permissions here are not a guarantee. Validate this directory on-device.
