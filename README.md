Free Agent Pelican theme
=========================

Pelican theme based on [Freelancer bootstrap theme ](http://ironsummitmedia.github.io/startbootstrap-freelancer/), which was ported to Pelican by [ondoheer](https://github.com/ondoheer/freelancer-theme-pelican/tree/master/templates) from the [Jekyll version](https://github.com/y7kim/agency-jekyll-theme).  
I modified it to resemble [Agency bootstrap theme](http://ironsummitmedia.github.io/startbootstrap-agency/), so I named it "Free Agent", since it's kind of a "Frankenstein's monster" of the two themes.  
This README is based on [Jerome Lachaud](https://github.com/jeromelachaud/freelancer-theme)'s

## How to use
 - Replace `/images/header-bg.png` with the image of your choice
 - Place portfolio images in `content/images/portoflio/`
 - Create posts to display your projects. Use the follow as an example:

```
---
Title: My first post
Date: 2010-12-12
Image: cabin.png
Client: Start Bootstrap
Client_Link: http://www.demo.com
Service: Web development
Here comes the content of my modal "article"... Cred flexitarian meditation, ugh put a bird on it lomo biodiesel disrupt freegan banjo viral. Banjo whatever sriracha paleo. Thundercats hella pour-over, plaid disrupt fixie typewriter tofu ugh viral seitan narwhal.
---  
```


## Contact form
There are two ways to use the contact form section.  
### Default
The default is already in the index.html file.  
It utilizes the static/js/contact_me.js script and passes the form  POST data to `static/mail/contact_me.php`.  
`contact_me.php` uses curl to send the form data via sendgrid (or mandrill et al)
#### contact_me.js
 - edit the `url:` to point to your domain  

#### contact_me.php
 - edit the variables necessary to use sendgrid, mandrill etc.

### Alternate contact form
 `templates/contact_static.html` is designed to use services like [formspree](http://formspree.io) via a form action.  
  - edit `index.html` and replace the `<!--contact form -->` section with:  
   `{% include 'contact_static.html'}`  
  - edit `templates/contact_static.html` to use your online form service of choice.

## footer  
The footer uses font awesome icons for the social links  


## Screenshot
![screenshot](/screenshot-freeagent.png)  

View this Pelican theme in action [here](http://callmefish.com)




=========
For more details, read [documentation](http://pelican.readthedocs.org)
