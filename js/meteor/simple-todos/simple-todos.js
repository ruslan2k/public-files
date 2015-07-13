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
      var new_item = {};
      new_item[key] = "";

      Items.insert(new_item);

      event.target.key.value = "";

      return false;
    },

    "focusout .key-value": function (event) {
      var key = event.target.dataset.key;
      var text = event.target.value;
      var new_item = {};
      new_item[key] = text;
      console.log(new_item);
      // FIXME
    },

    "click .delete": function () {
      Items.remove(this._id);
      //console.log(this._id);
    }

  });

  Template.single_item.helpers({
    isIndex: function (key) {
      var re = /^_id$/;
      if (re.exec(key)) {
        return true;
      }
      //console.log(key);
      return false;
    }
  });
}


