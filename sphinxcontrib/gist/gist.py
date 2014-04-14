#-*- coding:utf-8 -*-

from docutils import nodes

from docutils.parsers import rst


class gist(nodes.General, nodes.Element):
    filename = ""



def visit(self, node):

    if node.filename is not None:
        tag = u'''<script
        src="{0}.js?file={1}">&nbsp;</script>'''.format(node.url, 
                node.filename)
    else:
        tag = u'''<script src="{0}.js">&nbsp;</script>'''.format(node.url)

    self.body.append(tag)



def depart(self, node):
    pass



class GistDirective(rst.Directive):

    name = 'gist'
    node_class = gist

    has_content = False
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = False
    option_spec = {}


    def run(self):

        node = self.node_class()

        node.url = self.arguments[0]
        if len(self.arguments) > 1:
            node.filename = self.arguments[1]

        return [node]

