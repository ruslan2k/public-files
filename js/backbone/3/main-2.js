/**
 *
 */


var SingleLink = Marionette.ItemView.extend({
  tagName: "li",
  //template: '#template-myItemView',
  template: function (serialized_model) {
    //return JSON.stringify(serialized_model);
    return _.map(serialized_model, function (val, key) {
      return JSON.stringify(key)
        + JSON.stringify(val);
    });
    //return serialized_model.a;
  }
  //template: _.template("<a href='<%-path%>'><%-path%></a>")
  //template: function (model) {
  //  return "=>" + JSON.stringify(model);
  //  if (model !== null && typeof model === 'object') {
  //    return "[+]";
  //  } else {
  //    return typeof model;
  //  }
  //  //return "" + JSON.stringify(model);
  //}


});

var ListView = Marionette.CollectionView.extend({
  tagName: 'ul',
  childView: SingleLink
});

var teeData = [
  {a: "a1"},
  {a: "a2", b: [2, 3, 4]},
  {a: "a3", c: {d: 5}}
];

var list = new Backbone.Collection(_.map(teeData, function (item) {
  var new_model = new Backbone.Model(item);
  console.log(JSON.stringify(new_model.attributes));
  console.log(JSON.stringify(typeof new_model.attributes.a));
  return new_model;
}));

var list = new Backbone.Collection(teeData);

(new ListView({
  collection: list,
  el: '.link-area'
})).render();






