$(function(){
    var CRApp = Backbone.Router.extend({
	routes: {
	    "resource/form(/:key)": "form",
	    "resource/delete/:key": "delete"
	},
	delete: function(key) {
	    console.log("hello: "+key);
	},
	form: function(key) {
	    console.log("form:" + key);
	    if (key == null){
		var formView = new document.ResourceFormView({});
		formView.render(true);
	    }
	    else
	    {
		var resource = document.Resources.get(key);
		console.dir(resource);
	    }
	},
	resource: function(key){}
    });
				      
    document.Router = new CRApp();
    Backbone.history.start();
});