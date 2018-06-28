var StoryListPage = {
	init: function() {
		this.$container = $('.story-container');
		this.render();
		this.bindEvents();
	},

	render: function() {
	},

};


$(document).ready(function() {
	StoryListPage.init();
});