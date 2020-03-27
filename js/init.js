
$(document).ready(function() {
	
	/* -------------------------------------------------------------------------------------------*/
	/* --------------------------------- Initialize Cufon Fonts ---------------------------------- */
	/* -------------------------------------------------------------------------------------------*/
		
	Cufon.replace('h1, h2.h-border, h3.h-border', { fontFamily: 'DilleniaUPC' });
	Cufon.replace('h2.jobtitle', { fontFamily: 'Orator Std' });
	
	/* -------------------------------------------------------------------------------------------*/
	/* --------------------------- Initialize Testimonial Transition ---------------------------- */
	/* -------------------------------------------------------------------------------------------*/
		
	$('#testimonials').bxSlider({ 
		mode: 'fade',
		auto: true,
		pause: 5000
	});
	
	/* -------------------------------------------------------------------------------------------*/
	/* ---------------------- Initialize grayscale to colored hover effect ---------------------- */
	/* -------------------------------------------------------------------------------------------*/
		
	$(".grayscale").hover(function() { //On hover...
		var thumbOver = $(this).find("img").attr("src"); //Get image url and assign it to 'thumbOver'
		//Set a background image(thumbOver) on the <a> tag - Set position to bottom
		$(this).find("span").css({'background' : 'url(' + thumbOver + ') no-repeat center bottom'});
			//Animate the image to 0 opacity (fade it out)
		$(this).find("span img").stop().fadeTo('normal', 0 , function() {
			$(this).hide() //Hide the image after fade
		});
	} , function() { 
			$(this).find("span img").stop().fadeTo('normal', 1).show();
	});
	
});

$(window).load(function(){

	/* -------------------------------------------------------------------------------------------*/
	/* ---------------------------- Initialize Progress bar animation --------------------------- */
	/* -------------------------------------------------------------------------------------------*/
	
	$('.progressValue').each(function() {
		var progressValue = $(this).find('span').text();
		progressValue = parseFloat(progressValue);
		progressValue = (progressValue / 100) * 180;
		
		progressValue = progressValue - 180;
		var newValue = "" + progressValue + "px 0px";
	
		$(this).css( {backgroundPosition: "-180px 0"} );
		$(this).stop().animate({backgroundPosition:"("+ newValue + ")"}, {duration:1500})

		if ($(this).find('span').attr('title')) {
			$(this).find('span').html($(this).find('span').attr('title'));
		}
	});	

});			