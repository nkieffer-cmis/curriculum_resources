$(function(){
    document.ResourceFormView = Backbone.View.extend({
	el: $("main"),
	template: _.template($('#resource-form').html(),{}),
	render: function(is_admin) {
	    //	this.model.is_admin = is_admin;
	    if (this.model == null)
	    {
		this.$el.html(this.template({is_admin: is_admin}));
	    }
	    return this;
	}
    });
    console.dir(document.ResourceFormView);
});