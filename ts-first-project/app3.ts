type StringOrNum = string | number;
let itemPrice: number;

const setItemPrice = (price: StringOrNum):void => {
    if (typeof price === 'string') {
        itemPrice = 0;   
    } else {
        itemPrice = price;       
    }
};

setItemPrice(50);

