jQuery(document).ready(function () {
    $(document).on("change", ".variation-radios input", function () {
      $('select[name="' + $(this).attr("name") + '"]')
        .val($(this).val())
        .trigger("change");
    });
  
    $(document).on("click", ".plus", function (e) {
      // replace '.quantity' with document (without single quote)
      $input = $(this).prev("input.qty");
      var val = parseInt($input.val());
      var step = $input.attr("step");
      step = "undefined" !== typeof step ? parseInt(step) : 1;
      $input.val(val + step).change();
    });
    $(document).on(
      "click",
      ".minus", // replace '.quantity' with document (without single quote)
      function (e) {
        $input = $(this).next("input.qty");
        var val = parseInt($input.val());
        var step = $input.attr("step");
        step = "undefined" !== typeof step ? parseInt(step) : 1;
        if (val > 0) {
          $input.val(val - step).change();
        } 
      }
    );

    $( "input.qty" ).change(function() {
        var max = parseInt($(this).attr('max'));
        var min = parseInt($(this).attr('min'));
        if ($(this).val() > max)
        {
            $(this).val(max);
        }
        else if ($(this).val() < min)
        {
            $(this).val(min);
        } 
    });   
  
    $("h1.product_title.entry-title").on("click", function () {
      $("#the_excerpt").modal("show");
    });
  
    $(document.body).on(
      "updated_cart_totals added_to_cart removed_from_cart ",
      function (e) {
        setTimeout(function () {
          var pmn_count = jQuery("p.pmn-header-cart-count").text();
          jQuery(
            ".pm-header-cart .site-header-cart .cart-contents span.count"
          ).html(pmn_count);
        }, 1000);
      }
    );
  
    $(document.body).on("wc_fragments_refreshed", function (Response) {
      setTimeout(function () {
        var pmn_count = jQuery("p.pmn-header-cart-count").text();
        jQuery(
          ".pm-header-cart .site-header-cart .cart-contents span.count"
        ).html(pmn_count);
      }, 1000);
    });
    
  
    
  });
  