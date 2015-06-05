/**
 *
 */


var SingleLink = Marionette.ItemView.extend({
  tagName: "li",
  //template: _.template("<a href='<%-path%>'><%-path%></a>")
  template: function(model){
    return JSON.stringify(model);
  }


});

var ListView = Marionette.CollectionView.extend({
  tagName: 'ul',
  childView: SingleLink
});

var teeData = [
  {a: 1},
  {b: [2, 3, 4]},
  {c: {d: {e: 5}}}
];

var list = new Backbone.Collection(teeData);

(new ListView({
  collection: list,
  el: '.link-area'
})).render();






