# from manim import *

# class SuperpositionOfWaves(Scene):
#     def construct(self):
#         # Step 1: Title Introduction
#         title = Text("Superposition of Two Waves", font_size=40,gradient = (BLUE, PURPLE))
#         self.play(Write(title))
#         self.wait(1)
#         self.play(FadeOut(title))
        
#         # Step 2: First Set of Graphs
#         graph1 = self.plot_wave(lambda x: 0.5*np.sin(3*x), BLUE, "0.5sin(3x)", UP)
#         graph2 = self.plot_wave(lambda x: 0.5*np.sin(6.6 * x + PI), GREEN, "0.5sin(6.6x + \\pi)", DOWN)
#         # superposition_1 = self.plot_wave(lambda x: 0.25*np.sin(0.5*x) + 0.25*np.sin(1.1 * x + PI), BLUE, "Superposition", DOWN*2)
#         self.wait(2)
#         ax1 = Axes(
#             x_range=[0, 4 * PI, PI / 4],
#             y_range=[-1, 2, 0.25],
#             axis_config={"include_numbers": True},
#         ).shift(UP)
#         ax2 = Axes(
#             x_range=[0, 4 * PI, PI / 4],
#             y_range=[-1, 2, 0.25],
#             axis_config={"include_numbers": True},
#         ).shift(DOWN)
#         x_val = PI
#         vertical_line1 = ax1.get_vertical_line(ax1.input_to_graph_point(x_val, graph1), color=RED)
#         vertical_line2 = ax2.get_vertical_line(ax2.input_to_graph_point(x_val, graph2), color=RED)
#         self.play(Create(vertical_line1), Create(vertical_line2))
#         label = MathTex("x = \\pi").next_to(vertical_line1, UP)
#         self.play(Write(label))
#         self.play(FadeOut(graph2))
#         self.play(FadeOut(graph1))

#         axes = Axes(
#             x_range=[0, 6],
#             y_range=[-1.5, 1.5],
#             axis_config={"color": GREY},
#         ).to_edge(DOWN)
#         sine_wave = axes.plot(lambda x: 0.5*np.sin(3 * x), color=BLUE, x_range=[0, 6])
#         cosine_wave = axes.plot(lambda x: 0.5*np.cos(6.6* x), color=GREEN, x_range=[0, 6])
#         combined_wave = axes.plot(lambda x: 0.5*np.sin(2 * np.pi * x) + 0.5 * np.cos(4 * np.pi * x), color=PURPLE, x_range=[0, 6])
#         self.play(Create(axes), run_time=1.5)
#         sine_label = Text(r"0.5sin(3x)", color=BLUE).next_to(sine_wave, UP)
#         cosine_label = Text(r"0.5cos(6.6x+pi)", color=PURPLE).next_to(cosine_wave, DOWN)
#         combined_label = Text("Superposition", font_size=30, color=GREEN).next_to(combined_wave, UP)

#         self.play(Create(sine_wave), Write(sine_label), run_time=2)
#         self.play(Create(cosine_wave), Write(cosine_label), run_time=2)
#         self.play(Transform(sine_wave, combined_wave), Transform(sine_label, combined_label), run_time=3)

        
#         # Step 3: Clear and Prepare for 4 Waves
#         self.play(*[FadeOut(mob) for mob in self.mobjects])
#         title_2 = Text("Superposition of 3 Waves", font_size=40, gradient=(BLUE, PURPLE))
#         self.play(Write(title_2))
#         self.wait(1)
#         self.play(FadeOut(title_2))
        
#         # Step 4: Second Set of Graphs
#         graph1 = self.plot_wave(lambda x: 0.1*np.sin(3*x), RED, "sin(3x)", UP*3.5)
#         graph2 = self.plot_wave(lambda x: 0.1*np.sin(6.6 * x + PI), GREEN, "sin(1.1x + \\pi)", UP*1.5)
#         graph3 = self.plot_wave(lambda x: 0.1*np.sin(9.55 * x + PI / 2), ORANGE, "sin(9.55x + \\frac{\\pi}{2})", DOWN*0.5)
#         superposition_final = self.plot_wave(lambda x: 0.1*np.sin(x) + 0.1*np.sin(2.2 * x + PI) + 
#                                                       0.1*np.sin(3.1 * x + PI / 2) + 0.1*np.sin(1.3 * x + PI / 4), 
#                                               BLUE, "Superposition", DOWN*2.5)
        
#         statement = Text("The superposition gets more and more complex", font_size=30).to_edge(DOWN)
#         self.play(Write(statement))
#         self.wait(3)
#         self.play(FadeOut(*self.mobjects))  # Clear all at the end

#     def plot_wave(self, function, color, label, shift):
#         ax = Axes(
#             x_range=[0, 4 * PI, PI / 4],
#             y_range=[-1, 2, 0.25],
#             axis_config={"include_numbers": True},
#         ).shift(shift)
        
#         graph = ax.plot(function, color=color)
#         graph_label = ax.get_graph_label(graph, label=label, x_val=PI / 2, direction=UP)
#         self.play(Create(ax), Create(graph), Write(graph_label))
#         return VGroup(ax, graph, graph_label)






 #NEW CODE------------------------------------>
from manim import *

class SuperpositionOfWaves(Scene):
    def construct(self):
        # Step 1: Title Introduction
        title = Text("Superposition of Two Waves", font_size=40, gradient=(BLUE, PURPLE))
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Step 2: First Set of Graphs
        ax1 = Axes(
            x_range=[0, 4 * PI, PI / 4],
            y_range=[-0.5, 0.5, 0.25],
            axis_config={"include_numbers": False},
        ).shift(UP*2)
        ax2 = Axes(
            x_range=[0, 4 * PI, PI / 4],
            y_range=[-0.5, 0.5, 0.25],
            axis_config={"include_numbers": False},
        ).shift(DOWN*2)

        # Define the graphs
        graph1 = ax1.plot(lambda x: 0.25 * np.sin(3 * x), color=BLUE)
        graph2 = ax2.plot(lambda x: 0.25 * np.sin(6.6 * x + PI), color=GREEN)

        # Create axes and graphs
        self.play(Create(ax1), Create(graph1), Create(ax2), Create(graph2))

        # Add vertical lines
        x_val = PI/2
        vertical_line1 = ax1.get_vertical_line(ax1.i2gp(x_val, graph1), color=RED)
        vertical_line2 = ax2.get_vertical_line(ax2.i2gp(x_val, graph2), color=RED)
        
        # line = Line(start=[x_val,0.25 * np.sin(3 * x_val),0],end =[x_val,0.25 * np.sin(6.6 * x_val + PI),0],color=RED)
        label = MathTex("x = \\frac{\\pi}{2}").next_to(vertical_line1, UP)
        self.wait(2)
        self.play(Create(vertical_line1), Create(vertical_line2), Write(label))
        # self.play(Create(line))
        self.wait(1)

        # Step 3: Fade out graphs and prepare for combined wave
        self.play(FadeOut(graph1), FadeOut(graph2), FadeOut(ax1), FadeOut(ax2),FadeOut(vertical_line1),FadeOut(vertical_line2),FadeOut(label))

        axes = Axes(
            x_range=[0, 6],
            y_range=[-1.5, 1.5],
            axis_config={"color": GREY},
        ).to_edge(DOWN)

        sine_wave = axes.plot(lambda x: 0.5 * np.sin(3 * x), color=BLUE, x_range=[0, 6])
        cosine_wave = axes.plot(lambda x: 0.5 * np.cos(6.6 * x), color=GREEN, x_range=[0, 6])
        combined_wave = axes.plot(lambda x: 0.5 * np.sin(3 * x) + 0.5 * np.cos(6.6 * x), color=PURPLE, x_range=[0, 6])

        sine_label = Text("0.5sin(3x)", color=BLUE).next_to(sine_wave, UP)
        cosine_label = Text("0.5cos(6.6x)", color=GREEN).next_to(cosine_wave, DOWN)
        combined_label = Text("Superposition", font_size=30, color=PURPLE).next_to(combined_wave, UP)

        self.play(Create(axes))
        self.play(Create(sine_wave), Write(sine_label), run_time=2)
        self.play(Create(cosine_wave), Write(cosine_label), run_time=2)
        self.play(Transform(sine_wave, combined_wave), Transform(sine_label, combined_label), run_time=3)
        vertical_line3 = axes.get_vertical_line(axes.i2gp(x_val, combined_wave), color=RED)
        self.play(Create(vertical_line3))
        self.wait(2)
        self.play(sine_wave.animate.set_opacity(0.3),FadeOut(sine_label))
        self.play(*[mobject.animate.to_edge(UP) for mobject in self.mobjects])



        new_wave = axes.plot(lambda x: 0.5 * np.sin(5.3 * x) + 0.5 * np.cos(7.1* x), color=PURPLE, x_range=[0, 6])
        new_wave_label = Text("New Wave", font_size=30, color=RED).next_to(new_wave, DOWN)
        self.play(Create(new_wave), Write(new_wave_label), run_time=2)



        # Clear all at the end
        self.play(*[FadeOut(mob) for mob in self.mobjects])

