let someValue: any;

someValue = {};
someValue = 5;
someValue = 'wow';

let price: number | string = 5;
price = 'free';
// price = false;

type StrOrNum = number | string;
let orderID: StrOrNum;
let totalCost: number;

const calculateTotalCost = (price: StrOrNum, qty: number):void => {

};

const findOrderID = (customer: {
    customerId: StrOrNum,
    name: string
},
    productId: StrOrNum
): StrOrNum => {
     return orderID;
 }

