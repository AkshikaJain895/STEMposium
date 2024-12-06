from manim import *

class FourierImageProcessing(Scene):
    def construct(self):
        # Title Animation
        title = Text("Image Processing using Fourier Transform").scale(0.8)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # Displaying Image (Resized to fit screen)
        image = ImageMobject("snake.jpg").scale(1.5)
        image.set_height(5)  # Adjust the height to fit on screen
        self.play(FadeIn(image))
        self.wait(1)

        # Breaking Image into Grids (Pixel Representation)
        rows, cols = 20, 20  # Number of grid squares
        image_width, image_height = image.get_width(), image.get_height()
        
        # Create a grid
        grid = VGroup(*[
            VGroup(*[
                Square(side_length=image_width / cols)
                for _ in range(cols)
            ]).arrange(RIGHT, buff=0)
            for _ in range(rows)
        ]).arrange(DOWN, buff=0)

        # Center grid on the image
        grid.move_to(image.get_center())
        self.play(Create(grid), run_time=3)
        self.wait(1)

        # Enlarge one square with the corresponding image portion visible
        target_square_row, target_square_col = 10, 10  # Choose a square in the middle
        square_size = image_width / cols

        # Coordinates of the target grid square's region in the image
        left = -image_width / 2 + target_square_col * square_size
        top = image_height / 2 - target_square_row * square_size

        # Create a cropped part of the image
        cropped_part = ImageMobject("snake.jpg")
        cropped_part.set_height(image.get_height())  # Match the original image height
        cropped_part.set_width(image.get_width())   # Match the original image width
        cropped_part.move_to(image.get_center())  # Align with the original image

        # Mask the cropped portion
        mask = Rectangle(width=square_size, height=square_size)
        mask.set_fill(color=BLACK, opacity=1)
        mask.move_to(image.get_center() + np.array([left + square_size / 2, top - square_size / 2, 0]))

        # Add cropped portion to enlarged square
        enlarged_square = Square(side_length=5)
        enlarged_image = cropped_part.copy().set_crop(top=top - square_size, bottom=top, left=left, right=left + square_size
        ).set_height(enlarged_square.get_height())

        enlarged_image.move_to(ORIGIN)  # Center it

        # Add text showing pixel intensity
        intensity_text = Text("Intensity = f(x, y)", font_size=24).next_to(enlarged_image, DOWN)

        # Display enlarged part
        self.play(FadeIn(enlarged_square), FadeIn(enlarged_image))
        self.play(Write(intensity_text))
        self.wait(3)

        self.play(FadeOut(enlarged_square), FadeOut(enlarged_image), FadeOut(intensity_text))
        self.wait(1)

        # Fourier Transform Application
        transform_text = Text("Applying Fourier Transform", font_size=28)
        self.play(Write(transform_text))
        self.wait(1)
        self.play(FadeOut(transform_text))

        # Show Processed Image
        processed_image = ImageMobject("processed_snake.jpg").scale(1.5)
        processed_image.set_height(5)  # Same size as the original image
        self.play(FadeTransform(image, processed_image))
        self.wait(2)

        # Applications of Image Processing
        applications = VGroup(
            Text("Low-pass filter: Retain low frequencies (blur the image).", font_size=24),
            Text("High-pass filter: Retain high frequencies (enhance edges).", font_size=24),
            Text("Band-pass filter: Retain frequencies within a range.", font_size=24),
            Text("Compression: Retain most significant frequencies.", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_edge(DOWN)
        
        self.play(Write(applications))
        self.wait(3)
