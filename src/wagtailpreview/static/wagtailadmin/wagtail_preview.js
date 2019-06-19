if (!String.prototype.endsWith) {
  String.prototype.endsWith = function(search, this_len) {
    if (this_len === undefined || this_len > this.length) {
      this_len = this.length;
    }
    return this.substring(this_len - search.length, this_len) === search;
  };
}

(function($) {
  document.addEventListener('click', function(event) {
    var id = event.target.id;

    if (id.endsWith('-preview')) {
      var el = $(event.target);
      var prefix = el.closest('[data-prefix]').attr('data-prefix');
      var inputs = $('[name^="' + prefix + '-value"]');

      var context = {};

      inputs.each(function() {
        var inputName = this.name;
        var inputValue = this.value;

        context[inputName] = inputValue;
      });

      alert(JSON.stringify(context));
    }
  });
})(jQuery);
