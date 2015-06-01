function displayObject (object) {
  if( typeof object === 'object')
}


var SingleLink = Marionette.ItemView.extend({
  tagName: "div",
  //template: _.template("<a href='<%-path%>'><%-path%></a>")
  //template: _.template(model)
  template : function (model) {
    console.log(model);
    var output_string = '';
    if(typeof model === 'object') {
      output_string += '<span>[+]</span>';
    }
    return output_string + JSON.stringify(model);
  }
});

var ListView = Marionette.CollectionView.extend({
  tagName: 'div',
  childView: SingleLink
});


var list = new Backbone.Collection([
  {path: 'http://google.com'},
  {path: 'http://mojotech.com'},
]);

(new ListView({
  collection: list,
  el: '.link-area'
})).render();


