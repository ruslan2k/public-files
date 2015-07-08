Items = new Mongo.Collection("items");

if (Meteor.isClient) {
  // This code only runs on the client
  Template.body.helpers({

    items: function () {
      return Items.find({});
    },

    view_item: function (item) {
      var objKeys = $.map(item, function (value, key) {
        return key;
      });
      var ret_val = $.map(objKeys, function (key) {
        //return JSON.stringify({"key": key, "val": item[key]});
        return {"key": key, "val": item[key]};
      });
      console.log(ret_val);
      return ret_val;
    }
  });

  Template.body.events({
    "submit .new-item": function (event) {

      var key = event.target.key.value;
      //console.log(key);
      var new_item = {};
      new_item[key] = "";

      Items.insert(new_item);

      //console.log(event);
      //console.log(event.target);

      //event.target.text.value = "";
      event.target.key.value = "";

      return false;
    },

    "focusout .key-value": function (event) {
      var text = event.target.value;
      console.log(text);
      console.log(event.target);
      console.log(event.target.dataset.key);
      //console.log(event.currentTarget);
      //console.log(event.currentTarget.dataset.key);
    },

    "click .delete": function () {
      Items.remove(this._id);
      //console.log(this._id);
    }

  });

}


