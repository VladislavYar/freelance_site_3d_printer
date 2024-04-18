const old_locations = $("#locations").val() ? $("#locations").val() : [];
const old_users = $("#users").val() ? $("#users").val() : [];
const max_files = $("#id_images").attr("max-files");
const no_image_carousel = '<img class="d-block w-100 img border border-1 rounded" src="/static/images/no_data.jpg" alt="нет данных">';
const old_src_user_image = $("#id_user_image").attr("src");
let params = new URLSearchParams(window.location.search);
let old_choice_min = Number($("#price").attr("min-price")); 
let old_choice_max = Number($("#price").attr("max-price"));
if (params.has("min_price"))
  old_choice_min = params.get("min_price");
if (params.has("max_price"))
  old_choice_max = params.get("max_price");
let new_choice_min = old_choice_min;
let new_choice_max = old_choice_max;


function filterOrders() {
  let price = $("#price").val();
  let regexp = new RegExp("\\d+", "g");
  price = Array.from(price.matchAll(regexp));
  let min_price = price[0] ? price[0] : Number($("#price").attr("min-price")); 
  let max_price = price[1] ? price[1] : Number($("#price").attr("max-price"));
  let locations = $("#locations").val() ? $("#locations").val() : [];
  let users = $("#users").val() ? $("#users").val() : [];
  let uri = "/" + "?min_price=" + min_price + "&max_price=" + max_price;
  uri += locations.length ? "&locations=" + locations : "";
  uri += users.length ? "&users=" + users : "";
  uri += $(".show").attr("id") == "orders" ? "&customer_tab=1" : "&customer_tab=0";
  window.location.replace(uri);
}


function activateButtonFilter(
  old_locations, old_users
) {
  let new_locations = $("#locations").val() ? $("#locations").val() : [];
  let new_users = $("#users").val() ? $("#users").val() : [];
  if (
    old_locations.toString() != new_locations.toString() ||
    old_users.toString() != new_users.toString() ||
    old_choice_min != new_choice_min ||
    old_choice_max != new_choice_max
  )
    $("#button-filter").attr("disabled", false);
  else
    $("#button-filter").attr("disabled", true);
}

function showModal() {
  let form_order = $("#formOrder");
  if (form_order.attr("errors") === "true")
    form_order.modal('show');
}

function validationPrice() {
  let valid_var = $(this).val();
  valid_var = valid_var.replace(/[^0-9]/g, "").replace(/^0+/, "");
  $(this).val(valid_var);
}

function validationImages() {
  let images = $("#id_images");
  let del_images = $(".delete_image:checked").length;
  let old_images = $(".delete_image").length;
  if ((images[0].files.length + old_images - del_images) > max_files) {
    images.val(null);
    $("#orderNewImageIndicators").html(no_image_carousel);
    images.attr("class", "form-control is-invalid")
    $("#images_errors").html("<ul><li>Изображений должно быть не больше 4.</li></ul>");
    return
  }
  images.attr("class", "form-control");
  $("#images_errors").html("");
}

function setOrderImage() {
  images = $("#id_images")[0].files;
  let length = images.length;
  let carousel = no_image_carousel;
  if (length) {
  let carousel_indicators = '<div class="carousel-indicators">';
  let carousel_inner = '<div class="carousel-inner">';
  for (i = 0; i < length; i++) {
    let src = URL.createObjectURL(images[i]);
    if (i === 0) {
      carousel_indicators += '<button type="button" data-bs-target="#orderNewImageIndicators" ' +
                              'data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>';
      carousel_inner += '<div class="carousel-item active"><img src="' + src + '" class="d-block w-100 img border border-1 rounded" alt="Изображение ' + (i + 1) + '"></div>'
    } else {
      carousel_indicators += '<button type="button" data-bs-target="#orderNewImageIndicators" data-bs-slide-to="' + i + '" aria-label="Slide ' + (i + 1) + '"></button>';
      carousel_inner += '<div class="carousel-item"><img src="' + src + '" class="d-block w-100 img border border-1 rounded" alt="Изображение ' + (i + 1) + '"></div>';
    }
  }
  carousel_indicators += '</div>';
  carousel_inner += '</div>';
  carousel = carousel_indicators + carousel_inner + 
              '<button class="carousel-control-prev" type="button" data-bs-target="#orderNewImageIndicators" data-bs-slide="prev">' +
              '<span class="carousel-control-prev-icon" aria-hidden="true"></span><span class="visually-hidden">Previous</span>' +
              '</button><button class="carousel-control-next" type="button" data-bs-target="#orderNewImageIndicators" data-bs-slide="next">' +
              '<span class="carousel-control-next-icon" aria-hidden="true"></span><span class="visually-hidden">Next</span></button>';
  }
  $("#orderNewImageIndicators").html(carousel);
}


function setUserImage() {
  image = $("#id_user_picture")[0].files[0];
  if(image)
    $("#id_user_image").attr("src", URL.createObjectURL(image));
  else
    $("#id_user_image").attr("src", old_src_user_image);
}


$(function() {
    $("#slider-range").slider({
      range: true,
      min: Number($("#price").attr("min-price")),
      max: Number($("#price").attr("max-price")),
      values: [old_choice_min, old_choice_max],
      slide: function(event, ui) {
        new_choice_min = ui.values[0];
        new_choice_max = ui.values[1];
        activateButtonFilter(
          old_locations, old_users
        )
        $("#price").val(ui.values[0] + "р." + " - " + ui.values[1] + "р.");
      }
    });
    $("#price").val($("#slider-range").slider("values", 0) + "р." +
      " - " + $("#slider-range").slider("values", 1) + "р.");
  });
$("#button-filter").on("click", filterOrders);
$("#locations").change(function() {
  activateButtonFilter(old_locations, old_users)
});
$("#users").change(function() {
  activateButtonFilter(old_locations, old_users)
});
$(window).on("load", showModal);
$("#id_price").on("input", validationPrice);
$("#id_images").on("change", validationImages);
$("#id_images").on("change", setOrderImage);
$("#id_user_picture").on("change", setUserImage);
$(".delete_image").change(validationImages);