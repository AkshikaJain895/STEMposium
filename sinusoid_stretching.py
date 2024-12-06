from manim import *

class SinusoidFrequencyDemo(Scene):
    def construct(self):
        # Create Axes
        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-2, 2, 1],
            axis_config={"include_numbers": False},
        ).to_edge(DOWN)

        # Original Sinusoid
        original_sinusoid = axes.plot(lambda x: np.sin(2*PI*x), color=BLUE, x_range=[0, 2 * PI])
        original_label = axes.get_graph_label(original_sinusoid, "sin(x)", x_val=PI, direction=UP)

        # Plot Original
        self.play(Create(axes), Create(original_sinusoid), Write(original_label))
        self.wait(1)

        # Stretched Sinusoid (Lower Frequency)
        stretched_sinusoid = axes.plot(lambda x: np.sin(0.5 *2*PI* x), color=GREEN, x_range=[0, 2 * PI])
        stretched_label = axes.get_graph_label(stretched_sinusoid, "Lower Frequency", x_val=PI, direction=DOWN*3.2)

        # Transform to Stretched
        self.play(Transform(original_sinusoid, stretched_sinusoid),
                  Transform(original_label, stretched_label))
        self.wait(1)

        # Compressed Sinusoid (Higher Frequency)
        compressed_sinusoid = axes.plot(lambda x: np.sin(4*PI* x), color=ORANGE, x_range=[0, 2 * PI])
        compressed_label = axes.get_graph_label(compressed_sinusoid, "Higher Frequency", x_val=PI / 2, direction=UP)

        # Transform to Compressed
        self.play(Transform(original_sinusoid, compressed_sinusoid),
                  Transform(original_label, compressed_label))
        self.wait(1)

        # Fade Out
        self.play(FadeOut(axes), FadeOut(original_sinusoid), FadeOut(original_label))
