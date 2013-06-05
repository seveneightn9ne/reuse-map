$ = jQuery

function loadIframe(){
	console.log("loadIframe()")
	//$.get("server.py", function(data){
		$iframe = $("#whereis")
		//render dots
		new_url = "http://whereis.mit.edu?go=32&go=7&go=64"
		$iframe.attr("src",new_url)
		$iframe.load(function(){
			renderIframe(this)
		})
	//});
}
function renderIframe(iframe){
	console.log("renderIframe()")
	//makepretty(iframe)

}
$(document).ready(function(){
	loadIframe()
})
// $("iframe#whereis").load(function(){
// 	console.log("iframe.load()")
// 	//make pretty
// })