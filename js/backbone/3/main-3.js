/**
 *
 */

var myModel = new Backbone.Model({foo: "bar", baz: "qux"});

var KeyValueView = Marionette.ItemView.extend({
  el: "#model-area",
  ui: {
  },
  template: function (model) {
    var $my_template = $("#some-template");
    var new_model = _.map(model, function (val, key) {
      return {new_key: key, new_val: val}; 
    });
    console.log(JSON.stringify(new_model));
    return _.template($my_template.html(), {items: new_model});
  },
  events: {
    "focusout .model-val": "onEditFocusout",
  },

  onEditFocusout: function (e) {
    console.log(e.srcElement);
    console.log(e.type, e.target);
    console.log(e.type, e.target.key);
    console.log(e.result, e.data, e.currentTarget);
    console.log(e.relatedTarget);
    console.log(JSON.stringify(e.target));
    //var valueText = this.ui.value.val().trim();
    //console.log(valueText);
  }
});



var view = new KeyValueView({
  model: myModel
  //collection: myModel
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


