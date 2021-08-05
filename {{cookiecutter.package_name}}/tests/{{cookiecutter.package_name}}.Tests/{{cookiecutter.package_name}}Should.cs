using FluentAssertions;
using Xunit;

namespace {{cookiecutter.package_name}}.Tests
{
    public class {{cookiecutter.package_name}}Should
    {
        [Fact]
        public void run_successfully() 
        {
            var foo = new Foo();

            var actual = foo.Bar();

            actual.Should().Be("Baz");
        }
    }
}

