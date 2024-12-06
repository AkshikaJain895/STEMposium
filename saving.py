# NEW CODE FROM HERE
# from manim import *

# class FourierImageProcessing(Scene):
#     def construct(self):
#         # Title Animation
#         title = Text("Image Processing using Fourier Transform", gradient=(BLUE, PURPLE)).scale(0.8)
#         self.play(Write(title))
#         self.wait(1)
#         self.play(title.animate.to_edge(UP))
#         self.wait(1)
        
#         # Displaying Image (Resized to fit screen)
#         image = ImageMobject("snake.jpg").scale(1.5)
#         image.set_height(5)  # Adjust the height to fit on screen
#         self.play(FadeIn(image))
#         self.wait(1)

#         # Breaking Image into Grids (Pixel Representation)
#         rows, cols = 20, 20  # Adjust the number of grid squares
#         image_width, image_height = image.get_width(), image.get_height()

#         grid = VGroup(*[
#             VGroup(*[
#                 Square(side_length=image_width / cols)
#                 for _ in range(cols)
#             ]).arrange(RIGHT, buff=0)
#             for _ in range(rows)
#         ]).arrange(DOWN, buff=0)

#         # Center grid on the image
#         grid.move_to(image.get_center())
#         self.play(Create(grid), run_time=3)
#         self.wait(1)

#         # Enlarge one square to show pixel representation
#         self.play(FadeOut(image))
#         target_square = grid[10][10]  # Choose a square in the middle
#         enlarged_square = target_square.copy().scale(5).move_to(ORIGIN)
#         intensity_text = Text("Intensity = f(x, y)", font_size=24).next_to(enlarged_square, DOWN)

#         self.play(FadeIn(enlarged_square))
#         self.play(Write(intensity_text))
#         self.wait(3)

#         self.play(FadeOut(enlarged_square), FadeOut(intensity_text))
#         self.wait(1)

#         # Fourier Transform Application
#         transform_text = Text("Applying Fourier Transform", font_size=28)
#         self.play(Write(transform_text))
#         self.wait(1)
#         self.play(FadeOut(transform_text))

#         # Show Processed Image
#         processed_image = ImageMobject("processed_snake.jpg").scale(1.5)
#         processed_image.set_height(5)  # Same size as the original image
#         self.play(FadeTransform(image, processed_image))
#         self.wait(2)

#         # Applications of Image Processing
#         applications = VGroup(
#             Text("Low-pass filter: Retain low frequencies (blur the image).", font_size=24),
#             Text("High-pass filter: Retain high frequencies (enhance edges).", font_size=24),
#             Text("Band-pass filter: Retain frequencies within a range.", font_size=24),
#             Text("Compression: Retain most significant frequencies.", font_size=24)
#         ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_edge(DOWN)
        
#         self.play(Write(applications))
#         self.wait(3)