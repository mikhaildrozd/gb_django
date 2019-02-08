var config = {
    selectors: {
        add: '.basket-item-add',
        delete: '.basket-item-delete',
        quantity: '.basket-item-quantity',
        price: '.basket-item-price',

    },
    urls: {
        add: '/basket/add/',
        update: '/basket/update/',
        delete: '/basket/remove/'
    }
};


$(document).ready(function () {
    $(config.selectors.add).on('click', function () {
        var item_id = $(this).data('id');
        var item_url = config.urls.add + item_id + "/";

        var parent_item = $(this).parents()[0]; // <li>
        var counter = $(parent_item).find(config.selectors.quantity);
        var price = $(parent_item).find(config.selectors.price);

        $.ajax({
            url: item_url,

            success: function (data) {
                counter.text(data.quantity)
                price.text(data.price)
            }
        });
    })
});


$(document).ready(function () {
    $(config.selectors.delete).on('click', function () {
        var item_id = $(this).data('id');
        var item_url = config.urls.delete + item_id + "/";

        var parent_item = $(this).parents()[0]; // <li>
        var counter = $(parent_item).find(config.selectors.quantity);
        var price = $(parent_item).find(config.selectors.price);

        $.ajax({
            url: item_url,

            success: function (data) {
                if (data.quantity < 1) {
                    $(parent_item).hide();
                }
                counter.text(data.quantity)
                price.text(data.price)

            }
        });
    })
});