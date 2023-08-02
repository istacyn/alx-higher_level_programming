$(document).ready(function () {
	$('#btn_translate').click(fetchTranslation);
	$('#language_code').keyup( function (event) {
		if (event === 13) {
			fetchTranslation();
		}
	});

	function fetchTranslation() {
		const languageCode = $('#language_code').val();
		$.getJSON(`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
		function(data) {
			$('#hello').text(data.hello);
		}
	});
});
