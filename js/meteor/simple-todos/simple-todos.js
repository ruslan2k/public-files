function abc () {
  console.log("abc");
}



if (Meteor.isClient) {
  // counter starts at 0
  Session.setDefault('counter', 0);

  Template.view_item.helpers({
    echo: function (param) {
      var objKeys = $.map(param, function (value, key) {
        return key;
      });
      return $.map(objKeys, function (key) {
        return JSON.stringify({"key": key, "val": param[key]});
      });
      //return "param: " + JSON.stringify(param);
    }
  });  

  Template.body.helpers({
    items: [
      {a: 1},
      {a: 2},
      {a: 3},
    ],
    display_a: function () {
      return "a";
    }
  });

  Template.hello.helpers({
    counter: function () {
      return Session.get('counter');
    }
  });

  Template.hello.events({
    'click button': function () {
      // increment the counter when button is clicked
      Session.set('counter', Session.get('counter') + 1);
    }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}


