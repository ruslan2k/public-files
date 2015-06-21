/**
 *
 */

var KeyValueView = Marionette.ItemView.extend({
  template: "#template-key-value"
});

var ItemView = Marionette.CollectionView.extend({
  childView: KeyValueView,
  childViewOptions: function(model, index) {
    return {
      key: "k",
      value: "value",
    }
  }
});
 

//new KeyValueView().render();

new ItemView().render();


