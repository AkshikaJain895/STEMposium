from manim import *

class VectorDecomposition3D(ThreeDScene):
    def construct(self):
        # Set up 3D axes
        axes = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[-3, 3],
            axis_config={"include_tip": True, "include_numbers": True},
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Define a random 3D vector
        vector = np.array([2, 1, 1])
        vector_obj = Arrow3D(
            start=ORIGIN, 
            end=vector, 
            color=RED, 
            thickness=0.02
        )
        
        # Label the vector
        vector_label = MathTex("\\vec{v}").set_color(RED)
        vector_label.move_to(vector + np.array([0.3, 0.3, 0.3]))
        vector_label.rotate(-self.camera.phi, axis=RIGHT).rotate(-self.camera.theta, axis=UP).rotate(PI/2, axis= RIGHT)



        self.add(axes, vector_obj, vector_label)

        # Decompose vector into components
        x_comp = Arrow3D(start=ORIGIN, end=[vector[0], 0, 0], color=GREEN)
        y_comp = Arrow3D(start=[vector[0], 0, 0], end=[vector[0], vector[1], 0], color=BLUE)
        z_comp = Arrow3D(start=[vector[0], vector[1], 0], end=vector, color=PURPLE)

        # Animate components and labels
        x_label = MathTex("x\\hat{i}").rotate(PI / 2, axis=RIGHT).rotate(-self.camera.theta, axis=UP).rotate(PI/2, axis= RIGHT).move_to(x_comp.get_end() + np.array([0.2, 0.2, 0]))
        y_label = MathTex("y\\hat{j}").rotate(-self.camera.theta, axis=UP).rotate(PI/2, axis= RIGHT).move_to(y_comp.get_end() + np.array([0.2, 0.2, 0]))
        z_label = MathTex("z\\hat{k}").rotate(-self.camera.phi, axis=RIGHT).rotate(-self.camera.theta, axis=UP).rotate(PI/2, axis= RIGHT).move_to(z_comp.get_end() + np.array([0.2, 0.2, 0.2]))

        self.play(Create(x_comp), Write(x_label), run_time=2)
        self.play(Create(y_comp), Write(y_label), run_time=2)
        self.play(Create(z_comp), Write(z_label), run_time=2)

        # Show the vector as a sum of components
        sum_label = MathTex(
            "\\vec{v} = x\\hat{i} + y\\hat{j} + z\\hat{k}"
        ).rotate(-self.camera.phi, axis=RIGHT).rotate(-self.camera.theta, axis=UP).rotate(PI/2, axis= RIGHT).set_color(ORANGE)
        sum_label.move_to(vector + np.array([0, 1, 0]))  # Position above components
        self.play(Write(sum_label))
        self.wait(2)

        # Clear the screen and demonstrate dot product
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)

        # Dot product setup
        vector_a = np.array([2, 1, 0])
        vector_b = np.array([1, 2, 0])

        vec_a = Arrow3D(start=ORIGIN, end=vector_a, color=RED).scale(2)
        vec_b = Arrow3D(start=ORIGIN, end=vector_b, color=BLUE).scale(2)
        angle_arc = Angle(Line(ORIGIN, vector_a), Line(ORIGIN, vector_b), radius=0.5, color=YELLOW)
        theta_label = MathTex("\\theta").rotate(-self.camera.phi, axis=RIGHT).rotate(-self.camera.theta, axis=UP).rotate(PI/2, axis= RIGHT).set_color(YELLOW).next_to(angle_arc, RIGHT)

        self.play(Create(vec_a), Create(vec_b), run_time=2)
        self.play(Create(angle_arc), Write(theta_label), run_time=2)

        # Dot product expression
        dot_product_expr = MathTex(
            "\\vec{a} \\cdot \\vec{b} = |\\vec{a}| |\\vec{b}| \\cos(\\theta)"
        ).rotate(-self.camera.phi, axis=RIGHT).rotate(-self.camera.theta, axis=UP).rotate(PI/2, axis= RIGHT).set_color(ORANGE)
        dot_product_expr.move_to([0, 1, 0])

        self.play(Write(dot_product_expr))
        self.wait(2)
