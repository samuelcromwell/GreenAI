/*-----------------------------------------------------------------

Template Name:  Green AI - Revolutionising Smart City Infrastructure
Author:  Gramentheme
Author URI: https://themeforest.net/user/gramentheme/portfolio
Developer: Kawser Ahmed Roni
Version: 1.0.0
Description: Green AI - Revolutionising Smart City Infrastructure

-------------------------------------------------------------------
CSS TABLE OF CONTENTS
-------------------------------------------------------------------

01. preloader
02. header
03. swiper slider
04. animated text with swiper slider
05. shop products count
06. image src change
07. hide & show a div
08. isotope
09. add class & remove class
10. magnificPopup
11. back to top
12. data backgrund
13. coundown by click
14. remove products
15. wow animation

------------------------------------------------------------------*/

(function ($) {
	("use strict");

	// Preloader area start here ***
	var windowOn = $(window);
	windowOn.on("load", function () {
		$("#loading").fadeOut(500);
	});
	// Preloader area end here ***

	// Header area start here ***
	// Menu bars start here
	$(".header-bar").on("click", function (e) {
		$(".main-menu, .header-bar").toggleClass("active");
	});
	// Menu bars end here

	// Mobile Menu Start here
	$(".main-menu li a").on("click", function (e) {
		var element = $(this).parent("li");
		if (element.hasClass("open")) {
			element.removeClass("open");
			element.find("li").removeClass("open");
			element.find("ul").slideUp(300, "swing");
		} else {
			element.addClass("open");
			element.children("ul").slideDown(300, "swing");
			element.siblings("li").children("ul").slideUp(300, "swing");
			element.siblings("li").removeClass("open");
			element.siblings("li").find("li").removeClass("open");
			element.siblings("li").find("ul").slideUp(300, "swing");
		}
	});
	// Mobile Menu end here

	// Menu Top Fixed Start here
	var fixed_top = $(".header-section");
	$(window).on("scroll", function () {
		if ($(this).scrollTop() > 300) {
			fixed_top.addClass("menu-fixed animated fadeInDown");
			fixed_top.removeClass("slideInUp");
			$("body").addClass("body-padding");
		} else {
			fixed_top.removeClass("menu-fixed fadeInDown");
			fixed_top.addClass("slideInUp");
			$("body").removeClass("body-padding");
		}
	});
	// Menu Top Fixed end here

	// Mega menu area start here
	$("#mega-menu-btn, .mega-menu-area").hover(
		function () {
			// Mouse over the button or the mega-menu - show the div
			$(".mega-menu-area").addClass("mega-menu-hover"); // Add the class
		},
		function () {
			// Mouse out from the button or the mega-menu - hide the div
			$(".mega-menu-area").removeClass("mega-menu-hover"); // Remove the class
		}
	);
	// Mega menu area end here
	// Header area end here ***

	// Scroll down area start here ***
	$("#scrollDown").on("click", function () {
		setTimeout(function () {
			$("html, body").animate({ scrollTop: "+=1000px" }, "slow");
		}, 1000);
	});
	// Scroll down area end here ***

	// Banner two slider area start here ***
	var sliderActive1 = ".banner-slider";
	var sliderInit1 = new Swiper(sliderActive1, {
		loop: true,
		slidesPerView: 1,
		speed: 2000,
		effect: "fade",
		autoplay: {
			delay: 5000,
			disableOnInteraction: false,
		},
		pagination: {
			el: ".banner-two__dot",
			clickable: true,
		},
	});
	// Here this is use for animate ***
	function animated_swiper(selector, init) {
		var animated = function animated() {
			$(selector + " [data-animation]").each(function () {
				var anim = $(this).data("animation");
				var delay = $(this).data("delay");
				var duration = $(this).data("duration");
				$(this)
					.removeClass("anim" + anim)
					.addClass(anim + " animated")
					.css({
						webkitAnimationDelay: delay,
						animationDelay: delay,
						webkitAnimationDuration: duration,
						animationDuration: duration,
					})
					.one("animationend", function () {
						$(this).removeClass(anim + " animated");
					});
			});
		};
		animated();
		init.on("slideChange", function () {
			$(sliderActive1 + " [data-animation]").removeClass("animated");
		});
		init.on("slideChange", animated);
	}
	animated_swiper(sliderActive1, sliderInit1);
	// Here this is use for animate ***
	var swiper = new Swiper(".banner-two__slider", {
		loop: "true",
		effect: "fade",
		speed: 2000,
		autoplay: {
			delay: 5000,
			disableOnInteraction: false,
		},
		pagination: {
			el: ".banner-two__dot",
			clickable: true,
		},
	});
	// Banner two slider area end here ***

	// Banner three slider area end here ***
	var sliderActive2 = ".banner-three__slider";
	var sliderInit2 = new Swiper(sliderActive2, {
		loop: true,
		slidesPerView: 1,
		effect: "fade",
		speed: 3000,
		autoplay: {
			delay: 7000,
			disableOnInteraction: false,
		},
		navigation: {
			nextEl: ".banner-three__arry-next",
			prevEl: ".banner-three__arry-prev",
		},
	});
	// Here this is use for animate ***
	function animated_swiper(selector, init) {
		var animated = function animated() {
			$(selector + " [data-animation]").each(function () {
				var anim = $(this).data("animation");
				var delay = $(this).data("delay");
				var duration = $(this).data("duration");
				$(this)
					.removeClass("anim" + anim)
					.addClass(anim + " animated")
					.css({
						webkitAnimationDelay: delay,
						animationDelay: delay,
						webkitAnimationDuration: duration,
						animationDuration: duration,
					})
					.one("animationend", function () {
						$(this).removeClass(anim + " animated");
					});
			});
		};
		animated();
		init.on("slideChange", function () {
			$(sliderActive2 + " [data-animation]").removeClass("animated");
		});
		init.on("slideChange", animated);
	}
	animated_swiper(sliderActive2, sliderInit2);
	// Banner three slider area end here ***

	// Banner five slider area end here ***
	var sliderActive3 = ".banner-five__slider";
	var sliderInit3 = new Swiper(sliderActive3, {
		loop: true,
		slidesPerView: 1,
		effect: "fade",
		speed: 3000,
		autoplay: {
			delay: 7000,
			disableOnInteraction: false,
		},
		navigation: {
			nextEl: ".banner-five__arry-next",
			prevEl: ".banner-five__arry-prev",
		},
	});
	// Here this is use for animate ***
	function animated_swiper(selector, init) {
		var animated = function animated() {
			$(selector + " [data-animation]").each(function () {
				var anim = $(this).data("animation");
				var delay = $(this).data("delay");
				var duration = $(this).data("duration");
				$(this)
					.removeClass("anim" + anim)
					.addClass(anim + " animated")
					.css({
						webkitAnimationDelay: delay,
						animationDelay: delay,
						webkitAnimationDuration: duration,
						animationDuration: duration,
					})
					.one("animationend", function () {
						$(this).removeClass(anim + " animated");
					});
			});
		};
		animated();
		init.on("slideChange", function () {
			$(sliderActive3 + " [data-animation]").removeClass("animated");
		});
		init.on("slideChange", animated);
	}
	animated_swiper(sliderActive3, sliderInit3);
	// Banner five slider area end here ***

	// Project slider area start here ***
	var swiper = new Swiper(".project-slider", {
		spaceBetween: 30,
		speed: 500,
		loop: "true",
		autoplay: {
			delay: 5000,
			disableOnInteraction: false,
		},
		pagination: {
			el: ".pegi-number",
			type: "fraction",
		},
		navigation: {
			nextEl: ".project-arry-next",
			prevEl: ".project-arry-prev",
		},
	});
	var swiper = new Swiper(".project-slider2", {
		spaceBetween: 20,
		speed: 500,
		simulateTouch: false,
		autoplay: {
			delay: 5000,
			disableOnInteraction: false,
		},
		loop: "true",
		pagination: {
			el: ".pegi-number",
			type: "fraction",
		},
		navigation: {
			nextEl: ".project-arry-next",
			prevEl: ".project-arry-prev",
		},
	});
	// Project slider area end here ***

	// Donation slider area start here ***
	var swiper = new Swiper(".donation__slider", {
		loop: "true",
		spaceBetween: 30,
		speed: 500,
		centeredSlides: true,
		autoplay: {
			delay: 3000,
			disableOnInteraction: false,
		},
		navigation: {
			nextEl: ".donation__arry-next",
			prevEl: ".donation__arry-prev",
		},
		breakpoints: {
			991: {
				slidesPerView: 3,
			},
			575: {
				slidesPerView: 1,
			},
		},
	});
	// Donation slider area end here ***

	// Hot item slider area start here ***
	var swiper = new Swiper(".hot-items__slider", {
		loop: "true",
		spaceBetween: 30,
		speed: 500,
		centeredSlides: true,
		autoplay: {
			delay: 3000,
			disableOnInteraction: false,
		},
	});
	// Hot item slider area end here ***

	// Donation slider area start here ***
	var swiper = new Swiper(".donation-five__slider", {
		loop: "true",
		spaceBetween: 30,
		speed: 500,
		centeredSlides: true,
		autoplay: {
			delay: 4000,
			disableOnInteraction: false,
		},
		navigation: {
			nextEl: ".donation__arry-next",
			prevEl: ".donation__arry-prev",
		},
		breakpoints: {
			1200: {
				slidesPerView: 4,
			},
			991: {
				slidesPerView: 3,
			},
			575: {
				slidesPerView: 2,
			},
		},
	});
	// Donation slider area end here ***

	// Service three slider area start here ***
	var swiper = new Swiper(".service-three__slider", {
		loop: "true",
		spaceBetween: 30,
		speed: 1000,
		centeredSlides: true,
		autoplay: {
			delay: 4000,
			disableOnInteraction: false,
		},
		breakpoints: {
			991: {
				slidesPerView: 2,
			},
			575: {
				slidesPerView: 1,
			},
		},
		pagination: {
			el: ".service-three__dot",
			clickable: true,
		},
	});
	// Service three slider area end here ***

	// Animal gallery slider area start here ***
	var swiper = new Swiper(".animal-gallery__slider", {
		loop: "true",
		spaceBetween: 30,
		speed: 1000,
		centeredSlides: true,
		autoplay: {
			delay: 3000,
			disableOnInteraction: false,
		},
		breakpoints: {
			991: {
				slidesPerView: 3,
			},
			768: {
				slidesPerView: 2,
			},
		},
		navigation: {
			nextEl: ".animal__arry-next",
			prevEl: ".animal__arry-prev",
		},
	});
	// Animal gallery slider area end here ***

	// Team slider area start here ***
	var swiper = new Swiper(".team__slider", {
		loop: "true",
		spaceBetween: 30,
		speed: 500,
		autoplay: {
			delay: 4000,
			disableOnInteraction: false,
		},
		breakpoints: {
			1200: {
				slidesPerView: 4,
			},
			768: {
				slidesPerView: 2,
			},
		},
		navigation: {
			nextEl: ".team__arry-next",
			prevEl: ".team__arry-prev",
		},
	});
	// Team slider area end here ***

	// Blog two slider area start here ***
	var swiper = new Swiper(".blog-two__slider", {
		loop: "true",
		spaceBetween: 30,
		speed: 500,
		centeredSlides: true,
		autoplay: {
			delay: 3000,
			disableOnInteraction: false,
		},
		navigation: {
			nextEl: ".donation__arry-next",
			prevEl: ".donation__arry-prev",
		},
		breakpoints: {
			1200: {
				slidesPerView: 4,
			},
			768: {
				slidesPerView: 2,
			},
		},
	});
	// Blog two slider area end here ***

	// Animal slider area start here ***
	var swiper = new Swiper(".animal__slider", {
		loop: "true",
		spaceBetween: 30,
		speed: 500,
		autoplay: {
			delay: 3000,
			disableOnInteraction: false,
		},
		breakpoints: {
			1200: {
				slidesPerView: 6,
			},
			768: {
				slidesPerView: 4,
			},
			320: {
				slidesPerView: 2,
			},
		},
	});
	// Animal slider area end here ***

	// Testimonial slider area start here ***
	var swiper = new Swiper(".testimonial__slider", {
		loop: "true",
		spaceBetween: 30,
		speed: 500,
		grabCursor: true,
		autoplay: {
			delay: 3000,
			disableOnInteraction: false,
		},
		pagination: {
			el: ".testimonial__dot",
			clickable: true,
		},

		breakpoints: {
			991: {
				slidesPerView: 2,
			},
			575: {
				slidesPerView: 1,
			},
		},
	});
	// Testimonial slider area end here ***

	// Testimonial two slider area start here ***
	var swiper = new Swiper(".testimonial-two__slider", {
		loop: "true",
		spaceBetween: 20,
		speed: 500,
		autoplay: {
			delay: 4000,
			disableOnInteraction: false,
		},
		pagination: {
			el: ".testimonial-two__dot",
			clickable: true,
		},
	});
	// Testimonial two slider area end here ***

	// Blog slider area start here ***
	var swiper = new Swiper(".blog__slider", {
		loop: "true",
		spaceBetween: 30,
		speed: 500,
		autoplay: {
			delay: 5000,
			disableOnInteraction: false,
		},
		pagination: {
			el: ".blog__dot",
			clickable: true,
		},
	});
	// Blog slider area end here ***

	// History slider area start here ***
	var swiper = new Swiper(".history__slider", {
		slidesPerView: "auto",
		freeMode: true,
		mousewheel: {
			releaseOnEdges: true,
			sensitivity: 2,
		},
		pagination: {
			el: ".history__pegi-number",
			type: "fraction",
		},
	});
	// History slider area end here ***

	// Shop single swiper slider area start here ***
	var swiper = new Swiper(".shop-slider-thumb", {
		loop: true,
		spaceBetween: 10,
		slidesPerView: 4,
		freeMode: true,
		watchSlidesProgress: true,
		navigation: {
			nextEl: ".right-arry",
			prevEl: ".left-arry",
		},
	});
	var swiper2 = new Swiper(".shop-single-slide", {
		speed: 1000,
		loop: "true",
		grabCursor: true,
		navigation: {
			nextEl: ".right-arry",
			prevEl: ".left-arry",
		},
		thumbs: {
			swiper: swiper,
		},
	});
	// Shop single swiper slider area end here ***

	// Product slider area start here ***
	var swiper = new Swiper(".product-slider", {
		loop: "true",
		spaceBetween: 30,
		speed: 500,
		autoplay: {
			delay: 3000,
			disableOnInteraction: false,
		},
		navigation: {
			nextEl: ".product-arry-next",
			prevEl: ".product-arry-prev",
		},
		breakpoints: {
			1200: {
				slidesPerView: 4,
			},
			992: {
				slidesPerView: 3,
			},
			575: {
				slidesPerView: 2,
			},
		},
	});
	// Product slider area end here ***

	// Shop count js area start here ***
	$(".quantity").on("click", ".plus", function (e) {
		let $input = $(this).prev("input.qty");
		let val = parseInt($input.val(), 10); // Specify base 10
		$input.val(val + 1).change();
	});
	$(".quantity").on("click", ".minus", function (e) {
		let $input = $(this).next("input.qty");
		var val = parseInt($input.val(), 10); // Specify base 10
		if (val > 0) {
			$input.val(val - 1).change();
		}
	});
	// Shop count js area end here ***

	// Image src js area start here ***
	$(document).on("click", ".changeImage", function () {
		// Get the image URL from the "data-image" attribute of the clicked button
		var newImage = $(this).data("image");

		// Define the fade duration in milliseconds (e.g., 1000ms for 1 second)
		var fadeDuration = 50; // Change this value to your desired duration

		// Fade out the current image with the specified duration
		$("#myImage").fadeOut(fadeDuration, function () {
			// Change the src attribute of the image
			$("#myImage").attr("src", newImage);

			// Fade in the new image with the specified duration
			$("#myImage").fadeIn(fadeDuration);
		});
	});
	// Image src js area end here ***

	// Image src and class add js area start here ***
	$(document).on("mouseenter", ".changeImage2", function () {
		var newImage = $(this).data("image");
		var fadeDuration = 200;

		$("#myImage2").fadeOut(fadeDuration, function () {
			$("#myImage2").attr("src", newImage);
			$("#myImage2").fadeIn(fadeDuration);
		});

		$(this).addClass("clicked");
		$(".changeImage2").not(this).removeClass("clicked");
	});
	// Image src and class add js area end here ***

	// Hide & show by toggle js area start here ***
	$(document).on("click", ".share-btn", function () {
		var target = $(this).data("target");
		$("#" + target).toggle();
	});
	// Hide & show by toggle js area end here ***

	// Hide & show by click js area start here ***
	$(document).on("click", ".share-btn", function () {
		var target = $(this).data("target");
		$("#" + target).toggle();
	});
	// Hide & show by click js area end here ***

	// Hide & show by clicks js area start here ***
	$(document).on("click", "#openButton", function () {
		$("#targetElement").removeClass("side_bar_hidden");
	});
	$(document).on("click", "#closeButton", function () {
		$("#targetElement").addClass("side_bar_hidden");
	});
	// Hide & show by clicks js area end here ***

	// Radio btn area start here ***
	$(document).ready(function () {
		$(document).on("click", ".radio-btn span", function () {
			$(this).toggleClass("radio-btn-active");
		});
	});
	// Radio btn area end here ***

	// Isotope area start here ***
	var $grid = $(".filter__items").isotope({});
	// click here
	$(".filter__list").on("click", "li", function () {
		var filterValue = $(this).attr("data-filter");
		$grid.isotope({ filter: filterValue });
	});
	// change is-checked class on buttons
	$(".filter__list").each(function (i, buttonGroup) {
		var $buttonGroup = $(buttonGroup);
		$buttonGroup.on("click", "li", function () {
			$buttonGroup.find(".active").removeClass("active");
			$(this).addClass("active");
		});
	});
	// Isotope area end here ***

	// Background image date area start here ***
	$("[data-background").each(function () {
		$(this).css(
			"background-image",
			"url( " + $(this).attr("data-background") + "  )"
		);
	});
	// Background image date area end here ***

	// Video popup area start here ***
	$(".video-popup").magnificPopup({
		type: "iframe",
		iframe: {
			markup:
				'<div class="mfp-iframe-scaler">' +
				'<div class="mfp-close"></div>' +
				'<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>' +
				"</div>",

			patterns: {
				youtube: {
					index: "youtube.com/",

					id: "v=",

					src: "https://www.youtube.com/embed/%id%?autoplay=1",
				},
				vimeo: {
					index: "vimeo.com/",
					id: "/",
					src: "//player.vimeo.com/video/%id%?autoplay=1",
				},
				gmaps: {
					index: "//maps.google.",
					src: "%id%&output=embed",
				},
			},

			srcAction: "iframe_src",
		},
	});
	// Video popup area end here ***

	// Map popup area start here ***
	$(".map-popup").magnificPopup({
		disableOn: 700,
		type: "iframe",
		mainClass: "mfp-fade",
		removalDelay: 160,
		preloader: false,
		fixedContentPos: false,
	});
	// Map popup area end here ***

	// Add payment amount area start here ***
	$(document).on("click", ".amount-btn", function () {
		// Remove the "active" class from all buttons
		$(".amount-btn").removeClass("active");

		// Add the "active" class to the clicked button
		$(this).addClass("active");

		// Get the text value of the clicked button
		var buttonValue = $(this).text();

		// Update the value attribute of the input element
		$(".addAmount-value").val(buttonValue);
	});
	// Add payment amount area end here ***

	// Payment button area start here ***
	$(document).on("click", ".payment-btn", function () {
		// Check if the clicked button already has the "active" class
		if ($(this).hasClass("active")) {
			// If it does, remove the "active" class
			$(this).removeClass("active");
		} else {
			// If it doesn't, remove the "active" class from all buttons
			$(".payment-btn").removeClass("active");
			// Add the "active" class to the clicked button
			$(this).addClass("active");
		}
	});
	// Payment button area end here ***

	// Counter up area start here ***
	$(".count").counterUp({
		delay: 20,
		time: 3000,
	});
	// Counter up area end here ***

	// Nice seclect area start here ***
	$(document).ready(function () {
		$("select").niceSelect();
	});
	// Nice seclect area end here ***

	// Footer image popup start here ***
	$(".footer-popup").magnificPopup({
		type: "image",
		gallery: {
			enabled: true,
		},
	});
	// Footer image popup end here ***

	// Back to top area start here ***
	var scrollPath = document.querySelector(".scroll-up path");
	var pathLength = scrollPath.getTotalLength();
	scrollPath.style.transition = scrollPath.style.WebkitTransition = "none";
	scrollPath.style.strokeDasharray = pathLength + " " + pathLength;
	scrollPath.style.strokeDashoffset = pathLength;
	scrollPath.getBoundingClientRect();
	scrollPath.style.transition = scrollPath.style.WebkitTransition =
		"stroke-dashoffset 10ms linear";
	var updatescroll = function () {
		var scroll = $(window).scrollTop();
		var height = $(document).height() - $(window).height();
		var scroll = pathLength - (scroll * pathLength) / height;
		scrollPath.style.strokeDashoffset = scroll;
	};
	updatescroll();
	$(window).scroll(updatescroll);
	var offset = 50;
	var duration = 950;
	jQuery(window).on("scroll", function () {
		if (jQuery(this).scrollTop() > offset) {
			jQuery(".scroll-up").addClass("active-scroll");
		} else {
			jQuery(".scroll-up").removeClass("active-scroll");
		}
	});
	jQuery(".scroll-up").on("click", function (event) {
		event.preventDefault();
		jQuery("html, body").animate(
			{
				scrollTop: 0,
			},
			duration
		);
		return false;
	});
	// Back to top area end here ***

	// WOW Animatin area start here ***
	new WOW().init();
	// WOW Animatin area start here ***
})(jQuery);
