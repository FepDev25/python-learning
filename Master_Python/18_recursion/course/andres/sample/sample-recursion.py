from course.andres.sample.recursion.models.component import Component

def recursive_function(c: Component, level: int = 0):
    print('\t' * level + c.name)
    c.level = level
    if c.has_children():
        for child in c.children:
            recursive_function(child, c.level + 1)

pc = Component('Gabinete PC ATX')

power = Component('Fuente poder 800w')
motherboard = Component('Mainboard Asus sockets Intel')
cpu = Component('CPU Intel i9')
fan = Component('Ventilador Cpu')
heatsink = Component('Disipador')
graphic_card = Component('Nvidia RTX 5090')
gpu = Component('Nvidia GPU')
gpu_ram = Component('8gb Ram')
gpu_ram2 = Component('8gb Ram')
gpu_fans = Component('Ventiladores GPU')
ram = Component('Memoria Ram 32GB')
ssd = Component('Disco Duro SSD 2T')

cpu.add_children(fan).add_children(heatsink)

(graphic_card.add_children(gpu)
 .add_children(gpu_ram)
 .add_children(gpu_ram2)
 .add_children(gpu_fans))

motherboard.add_children(cpu).add_children(graphic_card).add_children(ram).add_children(ssd)

(pc.add_children(motherboard)
 .add_children(power)
 .add_children(Component('Teclado'))
 .add_children(Component('Mouse')))

recursive_function(pc)