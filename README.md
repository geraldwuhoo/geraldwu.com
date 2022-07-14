# geraldwu.com

[![pipeline status](https://gitlab.wuhoo.xyz/jerry/geraldwu.com/badges/master/pipeline.svg)](https://git.wuhoo.xyz/jerry/geraldwu.com/-/commits/master)

## Why? The old website was nice and modern and responsive and flashy and \<insert buzzword here\>

**MODERN WEB RANT INCOMING**

Just take a look at my old website. It pulled all sorts of JavaScript libraries for JQuery, bootstrap, MDbootstrap, and external fonts from fontawesome and emoji-css. It had all sorts of buttons, smooth scrolling, and "responsive" design using bootstrap. All to simply display static text that could be easily read off of a résumé PDF. And at what cost? 2.60MB. A mostly text-only page, was *2.60MB*. This is a prime example of modern web bloat.

What's even worse about the old site, is that it was *dynamically generated*. Every time somebody hit my website, my web server would do a call to a MariaDB instance, fetch all the data with SQL queries, and process the final result. Only then would it send the actual page back to the client. For what reason did I do this? No really, why did I do this? The content was all static anyway. It simply wasted CPU cycles server-side.

The modern web is bloated with unnecessary JavaScript, external images, and other useless "features" that accomplish nothing except stress the CPU. Computers are powerful nowadays, but CPU cycles and network bandwidth aren't free.

Don't just take my rambling about it. Take a look at this report about trying to browse the modern web on a slow connection: https://danluu.com/web-bloat/. We are currently in an arms race to make "modern" website more flashy, responsive, and bloated for no reason other than to prove that we can. There is nothing wrong with a simple, text site to convey static information, and I will no longer support a bloated JavaScript web.

## The new website

The new website is a simple, JavaScript-free, text-based site. Just like the old days of the Internet where you didn't need a gigabit connection and a quad-core machine just to load a JavaScript-ridden modern website.

The website is statically generated based off a config file, located in `config.yaml`. This makes it very easy for me to add new entries to each section, simply by adding a very human-readable entry to the YAML file. Even someone with no coding experience whatsoever can easily read the `config.yaml` file.

To generate the static site, there is a small Python script `main.py` that generates the finished `index.html` using the jinja2 template located at `index.jinja2`.

The new `index.html` and `style.css` combined are less than 10KB! The final page with images is 361KB, but I have not yet optimized the images, which could be significantly shrunk and compressed. Nor have I applied gzip compression at the webserver level. And yet, this is already a significant improvement over the previously bloated 2.60MB of JavaScript. Not to mention, much easier on the CPU cycles since my server is only serving a static site, and the client is only rendering basic HTML and a little bit of CSS for formatting.

## The roadmap

- [x] Add "About Me" section
- [x] Add footer with contact info
- [x] Optimize images
- [x] GitLab CI/CD to automatically deploy changes to geraldwu.com
- [x] gzip compression at the webserver
