
####Uh, scratchpad to figure out various combination for bookmarkelt and what works. 

javascript:document.getElementsByTagName('body')%5B0%5D.appendChild(document.createElement('iframe')).setAttribute('src','https://www.mendeley.com/minified/bookmarklet.js');

javascript:(function(){var d=document,e=d.getElementsByTagName('body')[0];e.append="<h2>324</h2>";console.log('something is happening')})();

javascript:(function(){var d=document,e=d.getElementsByTagName('body');console.log(e[0]);var node = document.createElement("frame");node.setAttribute('src','https://commeta.herokuapp.com/');e[0].appendChild(node);console.log(window.location.href)})();

javascript:(function(){
	var d=document;
	e=d.getElementsByTagName('html');
	var frm=document.createElement("frameset");
	frm.setAttribute('cols','25%,*');
	var fr1 = document.createElement("frame");
	fr1.setAttribute('src',"https://commeta.herokuapp.com/anonchat/"+encodeURIComponent(window.location.href));
	var fr2=document.createElement("frame");
	fr2.setAttribute('src',window.location.href);frm.appendChild(fr1);frm.appendChild(fr2);d.replaceChild(frm,e[0]);
	console.log(e[0]);
	console.log(document.cookie);
})();

javascript:(function(){console.log(document.cookie);})();

javascript:(function(){
	//window.open("https://localhost:5000/chat/"+encodeURI(window.location.href));
	var xmlHttp = getNewHTTPObject(); //returns a XMLHttpRequest object
 
    function chargeURLPut(url) { 
        var mimeType = "text/plain";  
      xmlHttp.open('PUT', url, true);  // true : asynchrone false: synchrone
    xmlHttp.setRequestHeader('Content-Type', mimeType);  
    xmlHttp.send(null); 
 }
 console.log('asdsa');
})();


javascript:(function(){
	var d=document;
	var frame = document.createElement('iframe');
	frame.src= "https://commeta.herokuapp.com/anonchat/"+encodeURIComponent(window.location.href);
	frame.width = "350";
	frame.height = "250";
	frame.style.position = "fixed";
	frame.style.bottom = "30px";
	frame.style.right = "30px";
	frame.style.zIndex = "10";
	frame.style.border = "solid 2px #5bc0de";
	e=d.getElementsByTagName('body');
	document.body.insertBefore(frame, document.body.firstChild);

	

})();

javascript:(function(){window.open("https://commeta.herokuapp.com/chat/"+encodeURIComponent(window.location.href));})();

javascript:(function(){window.open("localhost:5000");})();



//document.body.insertBefore(frame, document.body.firstChild);