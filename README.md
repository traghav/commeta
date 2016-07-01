#Commeta

###Internet's own comment haven.

---

## Introduction

Commenting on the internet is broken. I elaborate on that and the various design decision I made [here](http://raghav.website/commeta).

A lot of work needs to be done to make this work universally and many bugs need to be squashed.
A neater implementation of this would be a browser extension but its currently implemented as a javascript bookmarket.
## Installation and usage

Select the piece of code below and drag it to your bookmark bar:
```javascript
javascript: (function() {
    var d = document;
    var frame = document.createElement('iframe');
    frame.src = "https://commeta.herokuapp.com/anonchat/" + encodeURIComponent(window.location.href);
    frame.width = "350";
    frame.height = "250";
    frame.style.position = "fixed";
    frame.style.bottom = "30px";
    frame.style.right = "30px";
    frame.style.zIndex = "40";
    frame.style.border = "solid 2px #5bc0de";
    e = d.getElementsByTagName('body');
    document.body.insertBefore(frame, document.body.firstChild);
})();
```
Click on the &#128196; 
when on a website and this should open a comment box. 


Credits to Zach Will's [Flask template](github.com/zachwill/flask_heroku) to get me started.
