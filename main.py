

from manim import *

class Q(MovingCameraScene):
    def construct(self):
        # Equation setup
        intro = Tex("Let's start our video",font_size=144,color=BLUE)
        self.play(Write(intro), run_time =6)
        self.play(FadeOut(intro))
        self.wait(2)
        # Let
        let = Tex("Let,").to_edge(UL)
        first_eq = MathTex("x^{3}+\\frac{3}{x}=","4(a^3+b^3)" "...(i)").to_edge(UL,buff = 1)
        second_eq = MathTex("\\frac{1}{x^3}+3x=","4(a^3-b^3)" "...(ii)").next_to(first_eq,DOWN)
        self.play(Write(let))
        self.play(Write(first_eq))
        self.play(Write(second_eq))
        ## adding and subtracting
        number = MathTex("(i)+(ii)").next_to(second_eq,DOWN).move_to([1,1,0])
        framebox1 = SurroundingRectangle(number, buff = .1)
        added_eq = MathTex("x^{3}","+" ,"\\frac{3}{x}" ,"+" ,"\\frac{1}{x^3}","+","3x","=","4(a^3+b^3)", "+","4(a^3-b^3)" )
        added_eq1 = MathTex("x^{3}","+" ,"3x" ,"+","\\frac{3}{x}","+", "\\frac{1}{x^3}","=","4(a^3+b^3)", "+","4(a^3-b^3)" )
        self.play(Write(number))
        self.play(Create(framebox1))
        self.play(Write(added_eq))
        self.wait(2)
        self.play(TransformMatchingTex(added_eq,added_eq1))
        equation = MathTex("x^{3}","+" ,"3\\times x^{2} \\times \\frac{1}{x}" ,"+","3\\times x\\times\\left(\\frac{1}{x}\\right)^{2} ","+", "\\left(\\frac{1}{x}\\right)^{3}","=","8a^3").next_to(added_eq1,DOWN)
        framebox2 = SurroundingRectangle(equation, buff = .1)
        
        self.play(Write(equation))
        self.wait(2)
        self.play(Create(framebox2))
        self.wait(2)
        self.play(FadeOut(Group(let,first_eq,second_eq,number,framebox1,added_eq1)))
        self.play(Group(equation,framebox2).animate.to_edge(UP))

        equation1 = MathTex("\\left(x+\\frac{1}{x}\\right)^{3} = 8a^3").next_to(equation,DOWN)
        
        equation2 =MathTex("\\left(x+\\frac{1}{x}\\right) = \\sqrt[3]{8a^3}").next_to(equation1,DOWN)
        equation3 = MathTex("\\left(x+\\frac{1}{x}\\right) = 2a").next_to(equation2,DOWN)
        self.play(Write(equation1))
        self.wait(2)
        self.play(Write(equation2))
        self.wait(2)
        self.play(Write(equation3))
        self.wait(2)
        self.play(FadeOut(Group(equation,equation1,equation2,equation3,framebox2)))




        ## minus
        let = Tex("Let,").to_edge(UL)
        first_eq = MathTex("x^{3}+\\frac{3}{x}=","4(a^3+b^3)" "...(i)").to_edge(UL,buff = 1)
        second_eq = MathTex("\\frac{1}{x^3}+3x=","4(a^3-b^3)" "...(ii)").next_to(first_eq,DOWN)
        self.play(Write(let))
        self.play(Write(first_eq))
        self.play(Write(second_eq))
        ## adding and subtracting
        number = MathTex("(i)-(ii)").next_to(second_eq,DOWN).move_to([1,1,0])
        framebox1 = SurroundingRectangle(number, buff = .1)
        added_eq = MathTex("x^{3}","+" ,"\\frac{3}{x}" ,"-" ,"\\frac{1}{x^3}","-","3x","=","4(a^3+b^3)", "-","4(a^3-b^3)" )
        added_eq1 = MathTex("x^{3}","-" ,"3x" ,"+","\\frac{3}{x}","-", "\\frac{1}{x^3}","=","4(a^3+b^3)", "-","4(a^3-b^3)" )
        self.play(Write(number))
        self.play(Create(framebox1))
        self.play(Write(added_eq))
        self.wait(2)
        self.play(TransformMatchingTex(added_eq,added_eq1))
        equation = MathTex("x^{3}","-" ,"3\\times x^{2} \\times \\frac{1}{x}" ,"+","3\\times x\\times\\left(\\frac{1}{x}\\right)^{2} ","-", "\\left(\\frac{1}{x}\\right)^{3}","=","8b^3").next_to(added_eq1,DOWN)
        framebox2 = SurroundingRectangle(equation, buff = .1)
        
        self.play(Write(equation))
        self.wait(2)
        self.play(Create(framebox2))
        self.wait(2)
        self.play(FadeOut(Group(let,first_eq,second_eq,number,framebox1,added_eq1)))
        self.play(Group(equation,framebox2).animate.to_edge(UP))

        equation1 = MathTex("\\left(x-\\frac{1}{x}\\right)^{3} = 8b^3").next_to(equation,DOWN)
        
        equation2 =MathTex("\\left(x-\\frac{1}{x}\\right) = \\sqrt[3]{8b^3}").next_to(equation1,DOWN)
        equation3 = MathTex("\\left(x-\\frac{1}{x}\\right) = 2b").next_to(equation2,DOWN)
        self.play(Write(equation1))
        self.wait(2)
        self.play(Write(equation2))
        self.wait(2)
        self.play(Write(equation3))
        self.wait(2)
        self.play(FadeOut(Group(equation,equation1,equation2,equation3,framebox2)))
        



        ##next part
        equation3 = MathTex("\\left(x+\\frac{1}{x}\\right)" ,"=" ,"2a  ... (i)").to_edge(UP)
        equation4 = MathTex("\\left(x-\\frac{1}{x}\\right)" ,"=" ,"2b   ... (ii)").next_to(equation3,DOWN)
      
        self.play(Write(equation3))
        self.wait(2)
      
        self.play(Write(equation4))
       
        self.wait(2)


        number = MathTex("(i)^{2}-(ii)^{2}").to_edge(UL)
        self.play(Write(number))
        framebox1 = SurroundingRectangle(number, buff = .1)
        self.play(Create(framebox1))
        self.wait(2)


        ##last


        e = MathTex("\\left(2a\\right)^2 - \\left(2b\\right)^2  = " ," \\left(x+\\frac{1}{x}\\right)^2 - \\left(x-\\frac{1}{x}\\right)^2")
        e1 = MathTex("4a^2 - 4b^2 = 4 \\times x\\times \\frac{1}{x} ").next_to(e,DOWN)
        e2 = MathTex("4\\left(a^2-b^2\\right) = 4").next_to(e1,DOWN)
        e3  = MathTex("\\therefore a^2-b^2 = 1").next_to(e2,DOWN)
        framebox3 = SurroundingRectangle(e3, buff = .1)
        self.play(Write(e))
        framebox2 = SurroundingRectangle(e[1], buff = .1)
        self.wait(2)
        self.play(Create(framebox2))
        self.wait(2)
        self.play(Write(e1))
        self.wait(2)
        self.play(Write(e2))
        self.wait(2)
        self.play(Write(e3))
        self.wait(2)
        self.play(Create(framebox3))
        self.wait(2)


        











