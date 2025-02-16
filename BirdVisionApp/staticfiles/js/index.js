// More API functions here:
			// https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image

			// the link to your model provided by Teachable Machine export panel
			const URL = 'https://teachablemachine.withgoogle.com/models/-1r0AX8_Z/';

			let model, labelContainer, maxPredictions;

			// Load the image model
			async function init() {
				const modelURL = URL + 'model.json';
				const metadataURL = URL + 'metadata.json';

				// load the model and metadata
				model = await tmImage.load(modelURL, metadataURL);
				maxPredictions = model.getTotalClasses();

				labelContainer = document.getElementById('label-container');
				for (let i = 0; i < maxPredictions; i++) {
					// and class labels
					labelContainer.appendChild(document.createElement('div'));
				}
			}

			async function predict() {
				// predict can take in an image, video or canvas html element
				var image = document.getElementById('imagePreview');
				const prediction = await model.predict(image, false);
                prediction.sort(function(a, b) {return b.probability - a.probability});
                let NUM_PREDICTIONS = 1
				for (let i = 0; i < NUM_PREDICTIONS; i++) {
					const classPrediction =
						prediction[i].className + ': ' + prediction[i].probability.toFixed(2);
					labelContainer.childNodes[i].innerHTML = classPrediction;
				}
			}

            const video = document.getElementById('video');
            const captureBtn = document.getElementById('captureBtn');
            const ctx = canvas.getContext('2d');
            const errorMessage = document.getElementById('errorMessage');
            const permissionBtn = document.getElementById('permissionBtn');
          
            // Function to start video stream from camera
            async function startCamera() {
              try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                video.srcObject = stream;
                // Hide error message and permission button if camera starts successfully
                errorMessage.classList.add('hidden');
                permissionBtn.classList.add('hidden');
              } catch (err) {
                console.error('Error accessing the camera: ', err);
                // Show error message and permission button
                errorMessage.textContent = 'Camera access is blocked. Please enable camera access to use this feature.';
                errorMessage.classList.remove('hidden');
                permissionBtn.classList.remove('hidden');
              }
            }
          
            permissionBtn.addEventListener('click', () => {
              startCamera();
            });
          
            // Capture image when the button is clicked and save it automatically
            captureBtn.addEventListener('click', () => {
              if (!video.srcObject) {
                  errorMessage.textContent = 'Please enable camera access first';
                  errorMessage.classList.remove('hidden');
                  return;
              }
              ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
              const imageData = canvas.toDataURL('image/png');  // Get the image data as a base64 URL
          
              // Create a File object from the base64 image data
              const byteString = atob(imageData.split(',')[1]);  // Decode base64 to binary
              const arrayBuffer = new ArrayBuffer(byteString.length);  // Create an ArrayBuffer
              const uint8Array = new Uint8Array(arrayBuffer);  // Create a Uint8Array
              for (let i = 0; i < byteString.length; i++) {
                  uint8Array[i] = byteString.charCodeAt(i);  // Convert each character to byte
              }
          
              // Create a Blob object from the Uint8Array (for use in file functions)
              const blob = new Blob([uint8Array], { type: 'image/png' });
              // Create a File object from the Blob
              const file = new File([blob], 'captured_image.png', { type: 'image/png' });
          
              // Call the readURL function with the created File object
              const fileInput = { files: [file] };  // Mocking the input.files property
              readURL(fileInput);  // Pass the file to the readURL function
          });
          
            window.onload = startCamera;