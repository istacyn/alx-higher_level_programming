$(document).ready(function () {
	$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', data => {
		$('#hello').text(data.hello);
	});
});
