$(function(){
	document.Resource = Backbone.Model.extend({
		defaults: function() {
			return {
				title: null,
				description: null,
				ts_created: null,
				ts_modified: null,
				creator: null,
				urls: null,
				tags: null,
				reviews: null };
		}
	});

	document.ResourceCollection = Backbone.Collection.extend({
		model: document.Resource,
		url: "/resource"
	});

	document.Resources = new document.ResourceCollection;
	document.ResourceView = Backbone.View.extend({
		el: $("#resources"),
		template: _.template($('#resource-tmp').html(),{}),
		render: function() {
			console.dir(this.model);
			this.$el.append(this.template(this.model));
			return this;
		}
	});

	document.Resources.fetch({
		success: function(collection, response, options){
			_.each(response, function(resource){
				var view = new document.ResourceView({model: resource});
				view.render();
			});
		}
	});
	console.dir(document.Resources.length);
	
	
});
