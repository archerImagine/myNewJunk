function getSpinner(){
   var counter = 0;
   function upper(){
      return ++counter;
   }
   function downer(){
      return --counter;
   }
   return {
      up : upper,
     down : downer
   }
}

var spinner = (function(){
   var counter = 0;
      return {
         up: function(){
         console.log(++counter);
      },
      down: function(){
         console.log(--counter);
      }
   }
}
)();