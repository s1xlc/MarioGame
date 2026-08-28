[app]
title = Mario Game
package.name = mariogame
package.domain = org.mariogame
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,wav,mp3,mp4
source.exclude_exts = spec
version = 0.1
requirements = python3,kivy,ffpyplayer
orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
