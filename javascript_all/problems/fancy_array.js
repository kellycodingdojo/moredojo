function prtArr(arr, rev) {
    if (rev == true) {
        for (var i = arr.length - 1; i >= 0; i--) {
            console.log(i + " -> " + arr[i]);
        }
      }
        else {
            for (var i = 0; i < arr.length; i++) {
                console.log(i + " -> " + arr[i]);
            }
      }
    }


prtArr(["hello", "bacon", "bits"],true);
