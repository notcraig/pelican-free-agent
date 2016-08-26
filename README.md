Free Agent Pelican theme
=========================

Pelican theme based on [Freelancer bootstrap theme ](http://ironsummitmedia.github.io/startbootstrap-freelancer/), which was ported to Pelican by [ondoheer](https://github.com/ondoheer/freelancer-theme-pelican/tree/master/templates) from the [Jekyll version](https://github.com/y7kim/agency-jekyll-theme).  
I modified it to resemble [Agency bootstrap theme](https://github.com/BlackrockDigital/startbootstrap-agency), so I named it "Free Agent", since it's kind of a "Frankenstein's monster" of the two themes.  
This README is based on [Jerome Lachaud](https://github.com/jeromelachaud/freelancer-theme)'s version.

## How to use
 - Replace `static/images/header-bg.png` with the image of your choice
 - Place portfolio images in `content/images/portoflio/`
 - Create posts to display your projects. Use the follow as an example:

```
---
Title: My first post
Date: 2016-12-12
Image: cabin.png
Client: Start Bootstrap
Client_Link: http://www.demo.com
Service: Web development
Here comes the content of my modal "article"... Cred flexitarian meditation, ugh put a bird on it lomo biodiesel disrupt freegan banjo viral. Banjo whatever sriracha paleo. Thundercats hella pour-over, plaid disrupt fixie typewriter tofu ugh viral seitan narwhal.
---  
```
## Configuration  
Several options can be configured in pelicanconf.py

The address in the footer:
```
ADDRESS1 = 'The Internet'
ADDRESS2 = 'Any City, Any Place'
```
The about page's left, right and center columns:  
```
ABOUT_LEFT = 'Take me to your leader! Switzerland is small and neutral! We are more like Germany, ambitious and misunderstood! I\'m Santa Claus! And so we say goodbye to our beloved pet, Nibbler, who\'s gone to a place where I, too, hope one day to go. The toilet.</p><p>Wow, you got that off the Internet? In my day, the Internet was only used to download pornography. <strong> I meant \'physically\'.</strong> <em> Look, perhaps you could let me work for a little food?</em> I could clean the floors or paint a fence, or service you sexually?</p><h3>Guess again.</h3>'

ABOUT_RIGHT = '<p>It\'s a fez. I wear a fez now. Fezes are cool. You know how I sometimes have really brilliant ideas? You know when grown-ups tell you \'everything\'s going to be fine\' and you think they\'re probably lying to make you feel better?</p><p>You hate me; you want to kill me! Well, go on! Kill me! KILL ME! It\'s art! A statement on modern society, \'Oh Ain\'t Modern Society Awful? \'! <strong> All I\'ve got to do is pass as an ordinary human being.</strong> <em> Simple.</em> What could possibly go wrong?</p><p>Father Christmas. Santa Claus. Or as I\'ve always known him: Jeff.</p>'

ABOUT_CENTER = '<a href="https://github.com/thetawavestudio" target="_blank" class="btn btn-lg btn-outline"><i class="fa fa-download">Go to my Github</i> </a>'
```

## Contact form
There are two ways to use the contact form section.  
### Default
The default utilizes the static/js/contact_me.js script and passes the form  POST data to `static/mail/contact_me.php`.  
`contact_me.php` uses curl to send the form data via sendgrid (or mandrill et al)
#### contact_me.js
 - edit the `url:` to point to your domain  (e.g., http://yourdomain.com/static/mail/contact_me.php)

#### contact_me.php
 - edit the variables necessary to use sendgrid, mandrill etc.

### Alternate contact form
 `templates/contact_static.html` is designed to use services like [formspree](http://formspree.io) via a form action.  
  - edit `index.html` and replace the `<!--contact form -->` section with:  
   `{% include 'contact_static.html'}`  
  - edit `templates/contact_static.html` to use your online form service of choice.






## Screenshots
**Landing:**  
![Landing Page](https://github.com/thetawavestudio/pelican-free-agent/blob/master/screenshots/landingpage.png)  
**Portfolio:**  
![Portfolio](https://github.com/thetawavestudio/pelican-free-agent/blob/master/screenshots/portfolio.png)  
**Modal:**
![Modal](https://github.com/thetawavestudio/pelican-free-agent/blob/master/screenshots/modal.png)  
**Contact:**  
![Contact](https://github.com/thetawavestudio/pelican-free-agent/blob/master/screenshots/contact.png) 
**Footer:**  
![Footer](https://github.com/thetawavestudio/pelican-free-agent/blob/master/screenshots/footer.png)  
**The whole shebang:**  
![Full Length](https://github.com/thetawavestudio/pelican-free-agent/blob/master/screenshots/full.png)  




=========
For more details, read the [documentation](http://pelican.readthedocs.org)
