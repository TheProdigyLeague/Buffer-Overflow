EyeWitness
===
EyeWitness is designed to take screenshots of websites. 
[!]: Provide Server--Header info
[!]: Identify default credentials.
~
EyeWitness is designed to run on Kali Linux. 
It will auto detect the file you give with -f flag...As being a .txt https://xxx.com/URLs 
>each new line...
>nmap xml output...or nessus xml output. 
# OPTIONAL: --timeout flag 
>Provide Max-Time Wait when Rendering and Screenshotting Web Page.
~
[!]:https://www.christophertruncer.com/eyewitness-2-0-release-and-user-guide/
# WIN
[+]: FortyNorthSecurity has created WIN_CLI (~Thanks (@Matt_Grandy_(c))
$ -docker --build /LOCALES/ -chek -release PATH/file/URL --scan
[!]: EyeWitness gen Report "AppData\Roaming" --dir 
[!]: Version_C#/EyeWitness Support parsing...taking screenshots of ie/chrome/bookmark. No supply list URL...Version_CobaltStrike code.exe -assembly.
# Setup:
1. CS dir nav
2. Load vs/EyeWitness.sln 
3. Go! Build top then Build Solution if no mods
~
# Usage:
```bash
$ EyeWitness.exe --help
$ EyeWitness.exe --bookmarks
$ EyeWitness.exe -f C:\Path\to\urls.txt
$ EyeWitness.exe --file C:\Path\to\urls.txt --delay [timeout in seconds] --compress
```
# Supported Linux Distros:
* Kali Linux
* Debian 7+ (at least stable, looking into testing) (Thanks to @themightyshiv)
* CentOS 7
* Rocky Linux 8
**E-Mail:** EyeWitness [@] christophertruncer [dot] com
# Setup:
1. .py/set-up dir nav
2. setup.sh/script.js "RUN"
# Usage:
```bash
$ ./EyeWitness.py -f filename --timeout optionaltimeout
```
# Examples:
```bash
$ ./EyeWitness -f urls.txt --web
$ ./EyeWitness -x urls.xml --timeout 8 
$ ./EyeWitness.py -f urls.txt --web --proxy-ip 127.0.0.1 --proxy-port 8080 --proxy-type socks5 --timeout 120
```
# BURP SUITE
SOCKS GUIDE ~thanks @raikia(c)
~~~
"Available here!!!" - https://github.com/FortyNorthSecurity/EyeWitness/issues/458
$ --git clone EyeWitness --apt from \sys32\BURP_SUITE 
~Thanks @digininja(c)
```bash
$ --APT
    /etc/apt/apt.conf.d/70proxy
        ~
$ cat /etc/apt/apt.conf.d/70proxy
Acquire::http::proxy "http://localhost:3128";
Acquire::https::proxy "https://localhost:3128";
$ --Git
~
$ cat ~/.gitconfig
[http]
proxy = http://localhost:3128
~
$ Wget
~
$ cat ~/.wgetrc or /etc/wgetrc
~
use_proxy=yes
http_proxy=127.0.0.1:3128
https_proxy=127.0.0.1:3128
~
..\gen\sys\burp_suite
~
export HTTP_PROXY=http://localhost:3128
export HTTPS_PROXY=http://localhost:3128
```
# Docker
$ eyewitness.exe --docker \container from --apt Dependencies ["HOST","m a c h i n e"]:
$ ..\docker\run.exe \folder\PATH ["HOST","m a c h i n e"]
(**/path/to/results**)  
$ eyewitness Scan \url from \file HKEY::VOLUME//folder if *urls.txt in */path/to/result then, arg *-f /tmp/EyeWitness/urls.txt*
# Usage
```bash
$ docker build --build-arg user=$USER --tag eyewitness --file ./Python/Dockerfile .
$ docker run \
    --rm \
    -it \
    -v /path/to/results:/tmp/EyeWitness \
    eyewitness \
    EyeWitness_flags_and_input
```
~
# Headless Capture
```bash
$ docker run \
    --rm \
    -it \
    -v ~/EyeWitness:/tmp/EyeWitness \
    eyewitness \
    --web \
    --single http://www.google.com
```
# Call to Action:
I'd love for EyeWitness to identify more default credentials of various web applications.  
As you find a device which utilizes default credentials, please e-mail me the source code of the index page and the default creds so I can add it in to EyeWitness!
