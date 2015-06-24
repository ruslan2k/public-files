/**
 *
 */

var MyModel = Backbone.Collection.extend();

var myModel = new MyModel([{foo: "bar"}]);

var KeyValueView = Marionette.ItemView.extend({
  //template: "#some-template",
  template: function (model) {
    var my_template = $("#my-template");
    var new_model = _.map(model, function (val, key) {
     return {new_key: key, new_val: val}; 
    });
    var template = _.template(my_template.html(), new_model);
  },
});



var view = new KeyValueView({
  collection: myModel
});

view.render();

//var ItemView = Marionette.CollectionView.extend({
//  childView: KeyValueView,
//  childViewOptions: function(model, index) {
//    return {
//      key: "k",
//      value: "value",
//    }
//  }
//});
 

//new KeyValueView().render();

//new ItemView().render();


