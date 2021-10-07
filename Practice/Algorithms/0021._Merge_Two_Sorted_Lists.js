/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *	 this.val = (val===undefined ? 0 : val)
 *	 this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
	let thisL1 = l1;
	let thisL2 = l2;
	let result = [];
	while ((thisL1 !== null && thisL1.val !== null) || (thisL2 !== null && thisL2.val !== null)) {
		if (thisL1 !== null && thisL1.val !== null && thisL2 !== null && thisL2.val !== null) {
			if (thisL1.val < thisL2.val) {
				result.push(thisL1.val);
				thisL1 = thisL1.next;
			} else {
				result.push(thisL2.val);
				thisL2 = thisL2.next;
			}
		} else if (thisL1 !== null && thisL1.val !== null) {
			result.push(thisL1.val);
			thisL1 = thisL1.next;
		} else {
			result.push(thisL2.val);
			thisL2 = thisL2.next;
		}
	}
	if (result.length == 0) {
		return null
	}
	let resultListNode = new ListNode(result[0])
	let thisNode = resultListNode;
	for (let i = 1; i < result.length; i++) {
		thisNode.next = new ListNode(result[i]);
		thisNode = thisNode.next
	}
	return resultListNode;
};
