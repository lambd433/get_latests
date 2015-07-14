#get_latests.py
Get the latest version URL from Index

##Usage
```shell
./get_latests.py [-s splitter] URL NAME.EXT
```
###Examples
```shell
./get_latests.py http://gstreamer.freedesktop.org/src/gst-plugins-base/
http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-0.9.7.tar.bz2.md5
http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-0.11.99.tar.xz.md5
http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-0.9.7.tar.gz
http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-0.9.7.tar.bz2
http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-1.5.2.tar.xz
http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-1.5.2.tar.xz.sha256sum
http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-0.9.7.tar.gz.md5
```

```shell
./get_latests.py http://gstreamer.freedesktop.org/src/gst-plugins-base/ gst-plugins-base.tar.xz
http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-1.5.2.tar.xz
```
