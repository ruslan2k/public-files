/**
 *
 */

var SingleLink = Marionette.ItemView.extend({
  tagName: "li",

  ui: {
    edit: '.edit',
    label: 'label',
    value: '.value',
    key: '.key',
  },

  events: {
    'dblclick @ui.label': 'onEditClick',
    'focusout @ui.value': 'onEditFocusout',
  },

  onEditClick: function () {
    this.$el.addClass('editing');
    this.ui.edit.focus();
    this.ui.edit.val(this.ui.edit.val());
  },

  onEditFocusout: function () {
    console.log(this.ui.value.val());
  },

  template: function (serialized_model) {
    //console.log(JSON.stringify(this));
    console.log(this.model);
    //return JSON.stringify(serialized_model);
    return _.map(serialized_model, function (val, key) {
      return "<span>" + key + "</span>:"
        + '<input class="value" " value="' + val + '"> ';
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


