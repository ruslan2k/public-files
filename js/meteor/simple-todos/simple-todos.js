if (Meteor.isClient) {
  // This code only runs on the client
  Template.body.helpers({
    tasks: [
      { text: "This is task 1", a: 11 },
      { text: "This is task 2", a: 21, b: 22 },
      { text: "This is task 3", a: 31, b: 32, c: 33 },
    ],

    items: [
      { name: "Ruslan", number: 42 },
      { name: "Ira", number: 911 },
    ],

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
    "submit .new-task": function (event) {

      var text = event.target.text.value;

      console.log(event);
      console.log(event.target);

      event.target.text.value = "";

      return false;

    },

    "focusout .key-value": function (event) {
      var text = event.target.value;
      console.log(text);
      console.log(event.target);
      console.log(event.currentTarget);
      console.log(event.currentTarget.dataset.key);
    }

  });

}


