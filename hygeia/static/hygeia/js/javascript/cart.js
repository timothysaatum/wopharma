
            const addCart = document.querySelectorAll(".order");

			for(var i = 0; i < addCart.length; i++){
				addCart[i].addEventListener('click', () => {
					cartCount();
				});
			}

			function cartCount() {
				let productNumbers = localStorage.getItem("cartNumber");
				productNumbers = parseInt(productNumbers);

				if(productNumbers) {
                  localStorage.setItem("cartNumber", productNumbers + 1);
				  document.querySelector(".nav span").textContent = productNumbers + 1;
				}
				else {
					localStorage.setItem("cartNumber", 1);
					document.querySelector(".nav span").textContent = 1;
				}

				
			}

			function decrease() {
				let productNumbers = localStorage.getItem("cartNumber");
				productNumbers = parseInt(productNumbers);

				if(productNumbers) {
                  localStorage.setItem("cartNumber", productNumbers - 1);
				  document.querySelector(".nav span").textContent = productNumbers - 1;
				}
				else {
					localStorage.setItem("cartNumber", 0);
					document.querySelector(".nav span").textContent = 0;
				}

				
			}
			
            window.onload = function loadCartNumbers(){
				let productNumbers = localStorage.getItem("cartNumber");
				if(productNumbers){
					document.querySelector('.nav span').textContent = productNumbers;
				}
			}
		   
			function deleteRow(o){
				var p = o.parentNode.parentNode;
				    p.parentNode.removeChild(p);
			}
            
			