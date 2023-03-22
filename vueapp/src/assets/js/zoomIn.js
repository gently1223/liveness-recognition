!function ($) {
	$.fn.zoomIn = function (options) {
		try {
			if (/*this.is('img')*/ true) {

				var
					timer = null,
					mouse = null,
					enableHandler = true,
					settings = $.extend({
						description: false,
						message: 'default message',
						transition: {
							time: '0.1s',
							type: 'ease-out'
						},
						step: 0.5,
						zoom: 2,
						zoomMax: 10,
						zoomMin: 1.5,
						rate: 80,
						callback: null
					}, options);



					return this.each(function () {

						var
							img = $(this),
							wrapper = img.wrap('<div class="zoomIn"></div>').parent();

						if (settings.description) {
							img.after('<div class="description"><h2>' + settings.message + '</h2><span class="zoom">' + settings.zoom + '</span></div>');
						}


						var getMousePosition = function ($this, event) {
							var
								mouseLeft = event.pageX - $this.offset().left,
								mouseTop = event.pageY - $this.offset().top;
							return {
								x: Math.floor(mouseLeft/ $this.width() * 100) + '%',
								y: Math.floor(mouseTop/ $this.height() * 100) + '%'
							}
						}


						wrapper.on('mouseenter', function (event) {
							mouse = getMousePosition(wrapper, event);
							img.css({
								'transform-origin': mouse.x + mouse.y,
								'transform': 'scale(' + settings.zoom + ')'
							});

							timer = setInterval(function (){
								enableHandler = true;
							}, settings.rate);
						});
						
						wrapper.on('mousemove', function (event) {
							if (enableHandler) {
								mouse = getMousePosition(wrapper, event);

								img.css({
									'transition': 'transform-origin ' + settings.transition.time + ' ' + settings.transition.type,
									'transform-origin': mouse.x + mouse.y
								});

								enableHandler = false;
							}
						});
						
						wrapper.on('mouseleave', function () {
							img.removeAttr('style');
							clearInterval(timer);
						});
						
						wrapper.on('DOMMouseScroll mousewheel', function(event) {
							if (event.originalEvent.detail > 0 || event.originalEvent.wheelDelta / 120 <= 0) {
								if (settings.zoom > settings.zoomMin) {
									settings.zoom -= settings.step;
								}
							} else {
								if (settings.zoom < settings.zoomMax) {
									settings.zoom += settings.step;
								}
							}
						
							img.css('transform', 'scale(' + settings.zoom + ')');
							wrapper.find('.zoom').html(settings.zoom.toFixed(2));
						
							return false;
						});
					});
			} else {
				throw 'Expected img, got: ' + this.get(0);
			}
		} catch (error) {
			console.log(error);
		}
	};
}(jQuery);