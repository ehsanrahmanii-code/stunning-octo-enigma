[app]
title = TITAN PRO
package.name = titanpro
package.domain = app.titanpro
source.dir = .
source.include_exts = py
version = 1.0.0
requirements = python3,flask,requests,numpy,pandas,websocket-client
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

p4a.bootstrap = webview
p4a.port = 8080
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = False
android.private_storage = False
